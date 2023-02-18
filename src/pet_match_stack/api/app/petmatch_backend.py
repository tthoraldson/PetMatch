import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import boto3
from botocore.config import Config
from boto3.dynamodb.conditions import Key
import requests
import json
import uuid
from typing import Union, Optional
import datetime
from typing import List, Dict
from enum import Enum
import math
import joblib
from config import shared_vars

# configure boto3
my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

origins = [
    '*'
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dynamo = boto3.client(
        'dynamodb', 
        # endpoint_url='http://dynamo:8001',
        config=my_config,
        # aws_access_key_id='DUMMYIDEXAMPLE',
        # aws_secret_access_key='DUMMYEXAMPLEKEY'
    )


# open model file(s)
cats_v2_bin_path = shared_vars['cats_v2_bin_path']
dogs_v2_bin_path = shared_vars['dogs_v2_bin_path']


# load models
collab_v2_dogs_model = joblib.load(dogs_v2_bin_path)
collab_v2_cats_model = joblib.load(cats_v2_bin_path)


class AnimalTypeEnum(str, Enum):
    cat = 'cat'
    dog = 'dog'

# these are the only string allowed for the 'option' parameter
class OptionEnum(str, Enum):
    collab = 'collab'
    content = 'content'


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello cats": b}

@app.get("/verify-dynamo")
def verify_dynamo():


    # insert the data into the table
    response = dynamo.list_tables()

    # check the status code of the response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Data inserted successfully!")
    else:
        print("Failed to insert data. Error: ", response)

    return json.dumps(response)

@app.get("/describe-dynamo")
def describe_dynamo():


    # insert the data into the table
    response = dynamo.describe_table(
        TableName='Cats-Adoptable'
    )
    # check the status code of the response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Data inserted successfully!")
    else:
        print("Failed to insert data. Error: ", response)

    print(response)
    return 'done'

class Ranking(BaseModel):
    user_id : str
    pet_id : str
    animal_type: AnimalTypeEnum
    response: bool

@app.post("/petmatch/put_ranking/")
async def petmatch_put_ranking(ranking:Ranking):

    rankings_table = 'Rankings'

    # define the data to be inserted into the table
    data = ranking.json()

    data = json.loads(data)

    # get current timestamp as  a string
    now = str(datetime.datetime.now())

    # insert the data into the table
    response = dynamo.put_item(
            TableName=rankings_table, 
            Item={
                'user_id': {'S': data['user_id']},
                'pet_id': {'S': data['pet_id']},
                'timestamp': {'S': now },
                'response' : {'BOOL': data['response']}
            }
        )

    # check the status code of the response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Data inserted successfully!")

        print("Getting next recommendation")
        new_recommendation = get_new_recommendation(
            user_id=1,
            animal_type='cat',
            option='collab'
        )

    else:
        print("Failed to save ranking. Error: ", response)

    return json.dumps( await new_recommendation)

class Preference(BaseModel):
    full_name : str
    email : str
    zip_code : int
    readiness : str
    age : int
    g_expression : Union[str,None] = None
    has_current_pets : Union[str,None] = None
    current_pets : Union[str,None] = None
    dog_size : Union[str,None] = None
    dog_energy : Union[str,None] = None
    dog_breed : Union[str,None] = None
    cat_size : Union[str,None] = None
    cat_energy : Union[str,None] = None
    cat_breed : Union[str,None] = None
    user_prefs : Union[list,None] = None

@app.post("/petmatch/put_preferences/")
def petmatch_put_preferences(prefs: Preference):

    users_table = 'UserPreferences'

    # define the data to be inserted into the table
    data = prefs.json()

    data = json.loads(data)

    # get current timestamp as  a string
    now = str(datetime.datetime.now())

    # insert the data into the table
    response = dynamo.put_item(
            TableName=users_table, 
            Item={
                'user_id': {'S': data['user_id']},
                'timestamp': {'S': now } ,
                'user_preferences' : {'S': json.dumps(data)}
            }
        )

    # check the status code of the response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Data inserted successfully!")
    else:
        print("Failed to insert data. Error: ", response)

    return json.dumps(response)


class UserFeedback(BaseModel):
    user_id: str
    score: float
    timestamp: str

@app.post("/petmatch/put_feedback")
def petmatch_put_feedback(feedback: UserFeedback):

    feedback_table = 'UserFeedback'

    # define the data to be inserted into the table
    data = feedback.json()

    data = json.loads(data)

    # get current timestamp as  a string
    now = str(datetime.datetime.now())

    # insert the data into the table
    response = dynamo.put_item(
            TableName=feedback_table, 
            Item={
                'user_id': {'S': data['user_id']},
                'timestamp': {'S': now } ,
                'score' : {'S': data['score']}
            }
        )

    # check the status code of the response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Data inserted successfully!")
    else:
        print("Failed to insert data. Error: ", response)

    return json.dumps(response)

def cleanNullTerms(d):
    clean = {}
    for k,v in d.items():
        if isinstance(v,dict):
            nested = cleanNullTerms(v)
            if len(nested.keys()) > 0:
                clean[k] = nested
        elif (v is not None) and (bool(v)): #filter out NAs and falses
            clean[k]= v 

    return clean


@app.get("/get_new_recommendation/{user_id}/{animal_type}")
async def get_new_recommendation(user_id: Union[str,int], animal_type: AnimalTypeEnum, option: OptionEnum):
    """
        
    Parameters: 
            user_id  = user_id (str or int)
            animal_type = specify cat or dog
            option: Enum (Collaborative filtering or content based filtering)
    Output: 
            new pet
                - pet id
                - image url (largest image)
                - pet description
                - pet attributes (if true)
            JSON
    """
    
    # TODO remove hard
    table_name = "Cats-Adoptable"
    full_photo_attr = 'primary_photo_cropped.full'
    option = option
    user_id = user_id
    # unmock
    # This mocks a request to predict_collab for 10 pets by method of collaborative filtering
    ten_pets = [ 58765130, 58957223, 58704541, 58725463, 58910057, 58710916, 58858666, 58688022, 58912182, 58964429]

    # Get recommendation 
    if option =='collab':
        ten_pets = predict_collab(user_id,10,animal_type)
        #print("here")
    elif option =='content':
        print('predict_content todo')

    return json.dumps(ten_pets)

    # build the keys
    keys : List[Dict] = [
            { 'pet_id': {'S': str(pet_id)}, 'animal_id': {'S': str(pet_id)} } for pet_id in ten_pets
        ]

    # TODO, remove this if we know the table name or animal type
    if animal_type=='cat':
        
        response=dynamo.batch_get_item(
            RequestItems={
                table_name: {
                    'Keys': keys
                }
            }   
        )

    # elif animal_type == 'dog' and option == 'collab':
    #     response =dynamo.batch_get_item(
    #         TableName=table_name,
    #         Key={
    #         'pet_id':{'S':animal_id},
    #         'animal_id':{'S':animal_id}
    #         }
    #     )

    # elif animal_type == 'dog' and option == 'content':
    #     response =dynamo.batch_get_item(
    #         TableName=table_name,
    #         Key={
    #         'pet_id':{'S':animal_id},
    #         'animal_id':{'S':animal_id}
    #         }
    #     )
    
    # load the database response as a python dict obj
    collab_animals : List = response['Responses'][table_name]
    
    for indx,_record in enumerate(collab_animals):
        
        collab_animals[indx].update(
            {'record': json.loads(collab_animals[indx]['record']['S'])}
        )

    animal_specs = [
        {
            'pet_id': animal['animal_id']['S'],
            'pet_description': animal['record']['description'],
            'full_photo': animal['record']['primary_photo_cropped.full'],
            'attrs': {
                'organization_id': animal['record']['organization_id'],
                'url': animal['record']['url'],
                'type': animal['record']['type'],
                'species': animal['record']['species'],
                'age': animal['record']['age'],
                'gender': animal['record']['gender'],
                'size': animal['record']['size'],
                'coat': animal['record']['coat'],
                'tags': animal['record']['tags'],
                'name': animal['record']['name'],
                'status': animal['record']['status'],
                'status_changed_at': animal['record']['status_changed_at'],
                'published_at': animal['record']['published_at'],
                'status': animal['record']['status'],
                'status_changed_at': animal['record']['status_changed_at'],
                'published_at': animal['record']['published_at'],
                'distance': animal['record']['distance'],
                'breeds.primary':  animal['record']['breeds.primary'],
                'breeds.secondary':  animal['record']['breeds.secondary'],
                'breeds.mixed':  animal['record']['breeds.mixed'],
                'breeds.unknown':  animal['record']['breeds.unknown'],
                'colors.primary':  animal['record']['colors.primary'],
                'colors.secondary':  animal['record']['colors.secondary'],
                'colors.tertiary':  animal['record']['colors.tertiary'],
                'attributes.spayed_neutered':  animal['record']['attributes.spayed_neutered'],
                'attributes.house_trained':  animal['record']['attributes.house_trained'],
                'attributes.declawed':  animal['record']['attributes.declawed'],
                'attributes.special_needs':  animal['record']['attributes.special_needs'],
                'attributes.shots_current':  animal['record']['attributes.shots_current'],
                'environment.children':  animal['record']['environment.children'],
                'environment.dogs':  animal['record']['environment.dogs'],
                'environment.cats':  animal['record']['environment.cats'],
                'contact.email': animal['record']['contact.email']
            }
        } for animal in collab_animals
    ]
    #clean null terms from dictionary
    for x in range(len(animal_specs)):
        to_clean = animal_specs[x]
        clean_animal_spec = cleanNullTerms(to_clean)
        animal_specs[x] = clean_animal_spec

    # dump as JSON to the API
    #return json.dumps(animal_specs)

@app.post("/get_url")
async def get_url(animal_id,animal_type='cat',animals_df=None):
    """
    Parameters: 
            animal_id  = animal id
            animals_df = dataframe of all animals of chosen type (dog, cat) 
            animal_type = specify cat or dog
    Output: 
            petfinder url of given animal_id
    """
    
    ds = animals_df
    colsGrab = ['url']
    if(animal_type=='cat'):
        response =dynamo.get_item(TableName="Cats-Adoptable",
                                  Key={'pet_id':{'S',animal_id},'pet_id':{'S',animal_id}}
                                  )
    #return ds.loc[ds['pet_id'] == animal_id][colsGrab].values[0]   
    return response[colsGrab].values[0] 


@app.post("/get_picture")
async def get_picture(animal_id,animal_type='cat',animals_df=None):  
    """
    Parameters: 
            animal_id  = animal id
            animals_df = dataframe of all animals of chosen type (dog, cat)
            animal_type = specify cat or dog 
    Output: 
            petfinder url of given animal_id
    """
    ds = animals_df
    colsGrab = 'primary_photo_cropped.full'

    if(animal_type=='cat'):
        response =dynamo.get_item(TableName="Cats-Adoptable",
                                  Key={
                                    'pet_id':{'S':animal_id},
                                    'animal_id':{'S':animal_id}
                                    }
                                  )
    #return ds.loc[ds['pet_id'] == animal_id][colsGrab].values[0]
    # load the database response as a python dict obj
    found_cat_pic = json.loads(response['Item']['record']['S'])

    # dump as JSON to the API
    return json.dumps(found_cat_pic[colsGrab])



def predict_collab(user_name,top_x,animal_type: AnimalTypeEnum,):
    """
    Parameters: 
            user_name    = string of user name
            top_x        = integer of how many recommendations to return
            animal_type = specify cat or dog
    Output: 
            top X recommendations in list form"""
    # get pet rankings for user for the animal type
    table_name = "Rankings"
    rankings_response=dynamo.query(
        TableName = table_name,
        KeyConditionExpression="user_id = :id",
        FilterExpression="contains(#animal_type,:animal_type)",
        ExpressionAttributeValues={
            ":id":{"S":user_name},
            ":animal_type":{"S":animal_type},
        },
        ExpressionAttributeNames={
            "#animal_type":"record",
        },
        #Select="user_id"        
    )

    output=rankings_response["Items"]
    #all_1user_rankings = pet_rankings[pet_rankings['user_name'] == user_name]
    #rankings_minusKnownbyUser = pd.concat([pet_rankings,all_1user_rankings], axis=0, ignore_index=True).drop_duplicates(subset=["user_name","animal_id"],keep=False, ignore_index=True) # only remove user specific rankings from overall list, not everyone's!
    #eligible_animals = rankings_minusKnownbyUser[['animal_id']]
    #eligible_animals['Estimate_Score'] = eligible_animals['animal_id'].apply(lambda x: animal_model.predict(user_name, x).est)
    #eligible_animals = eligible_animals.sort_values('Estimate_Score', ascending=False)
    #print(eligible_animals.head(top_x)) # get top X reccs
    #reccs= eligible_animals.head(top_x)['animal_id'].tolist()
    return output



def get_item_id(animal_id,animal_type='cat',animals_df=None):  
    """
    required by predict_content
    This method is required to translate from content-based model id for that animal and the petfinder data for that animal. 
    This ensures the correct petfinder data for the animal is retrieved and is a safety measure
    Parameters: 
            animal_id  = animal id
            animals_df = dataframe of all animals of chosen type (dog, cat)
            animal_type = specify cat or dog  
    Output: 
            petfinder id of animal from content-based recommender
    """
    ds = animals_df
    colsGrab = ['pet_id']
    if(animal_type=='cat'):
        response =dynamo.get_item(TableName="Cats-Adoptable",
                                  Key={'pet_id':{'S',animal_id},'pet_id':{'S',animal_id}}
                                  )
    #return ds.loc[ds['id'] == animal_id][colsGrab].values[0]
    return response[colsGrab].values[0]


@app.post("/predict_content")
async def predict_content(animal_id,animals_df,top_x,animal_model):
    """
    If you wish to debug the method, turn the print statements back on!
    Parameters: 
            animal_id    = animal id of what user liked already
            animals_df   = dataframe of all animals of chosen type (dog, cat)
            top_x        = integer of how many recommendations to return
            animal_model = pre-trained model to make recommendations with
    Output: 
            top X recommendations in list form
    """

    #print("Recommending " + str(top_x) + " animals similar to " + str(get_item_id(animal_id,animals_df)) + "... " 
    #      + get_picture(animal_id,animals_df) + " - " + get_url(animal_id,animals_df))   
    #print("-------")    
    reccs = animal_model[animal_id][:top_x]   
    reccstoOutput = []
    for rec in reccs: 
        #print("Recommended: " + str(get_item_id(rec[1],animals_df)) + " (score:" +      str(rec[0]) + ") " 
        #      + get_picture(rec[1],animals_df) + " - " + get_url(rec[1],animals_df))
        reccstoOutput.append(get_item_id(rec[1],animals_df)[0])
    return reccstoOutput


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086)