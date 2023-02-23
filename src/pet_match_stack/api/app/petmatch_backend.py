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
import pandas

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
    "http://localhost",
    "http://localhost:8086",
    "http://localhost:8501",
    "http://localhost:3000",
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
        endpoint_url='http://dynamo:8001',
        config=my_config,
        aws_access_key_id='DUMMYIDEXAMPLE',
        aws_secret_access_key='DUMMYEXAMPLEKEY'
    )


# open model file(s)
cats_v2_bin_path = '/src/app/models/collabfilter_model_cats_v2.pkl'
dogs_v2_bin_path = '/src/app/models/collabfilter_model_dogs_v2.pkl'
cats_v2_content_bin_path = '/src/app/models/cosine_similarity_model_catsv2.pkl'
dogs_v2_content_bin_path = '/src/app/models/cosine_similarity_model_dogsv2.pkl'

# load models
collab_v2_dogs_model = joblib.load(dogs_v2_bin_path)
collab_v2_cats_model = joblib.load(cats_v2_bin_path)
content_v2_dogs_model = joblib.load(dogs_v2_content_bin_path)
content_v2_cats_model = joblib.load(cats_v2_content_bin_path)

# load id files
cat_ids = joblib.load('/src/app/models/catIdsAll_nodupsmissingpics.pkl')
dog_ids = joblib.load('/src/app/models/dogsIdsAll_nodupsmissingpics.pkl')  

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
            option='collab',
            animal_id='000'
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
async def get_new_recommendation(user_id: Union[str,int], animal_type: AnimalTypeEnum, option: OptionEnum,animal_id: Union[str,int]):
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

    #table_name = "Cats-Adoptable"
    #full_photo_attr = 'primary_photo_cropped.full'
    option = option
    user_id = user_id
    animal_id = animal_id # only used by content-based filtering
    # This mocks a request to predict_collab for 10 pets by method of collaborative filtering
    #ten_pets = [ 58765130, 58957223, 58704541, 58725463, 58910057, 58710916, 58858666, 58688022, 58912182, 58964429]

    # Get recommendation 
    if option =='collab':
        ten_pets = predict_collab(user_id,50,animal_type)
    elif option =='content':
        ten_pets = predict_content(animal_id,10,animal_type)

    #return json.dumps(ten_pets) #debugging line

    # build the keys
    keys : List[Dict] = [
            { 'pet_id': {'S': str(pet_id)}, 'animal_id': {'S': str(pet_id)} } for pet_id in ten_pets
        ]

    if animal_type=='cat':
        table_name = "Cats-Adoptable"
        response=dynamo.batch_get_item(
            RequestItems={
                table_name: {
                    'Keys': keys
                }
            }   
        )
    elif animal_type == 'dog':
        table_name = "Dogs-Adoptable-master"
        response=dynamo.batch_get_item(
            RequestItems={
                table_name: {
                    'Keys': keys
                }
            }   
        )
    
    # load the database response as a python dict obj
    collab_animals : List = response['Responses'][table_name]
    
    for indx,_record in enumerate(collab_animals):
        
        collab_animals[indx].update(
            {'record': json.loads(collab_animals[indx]['record']['S'])}
        )

    if animal_type == 'cat': # need 2 versions because dogs augmented
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
    elif animal_type == 'dog': 
        animal_specs = [
            {
                'pet_id': animal['animal_id']['S'],
                'pet_description': animal['record']['description_x'],
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
                    'attributes.special_needs':  animal['record']['attributes.special_needs'],
                    'attributes.shots_current':  animal['record']['attributes.shots_current'],
                    'environment.children':  animal['record']['environment.children'],
                    'environment.dogs':  animal['record']['environment.dogs'],
                    'environment.cats':  animal['record']['environment.cats'],
                    'group': animal['record']['group'],
                    'grooming_frequency_category': animal['record']['grooming_frequency_category'],
                    'shedding_category': animal['record']['shedding_category'],
                    'energy_level_category': animal['record']['energy_level_category'],
                    'trainability_category': animal['record']['trainability_category'],
                    'demeanor_category': animal['record']['demeanor_category'],
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
    return json.dumps(animal_specs)

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



def predict_collab(user_name,top_x,animal_type: AnimalTypeEnum):
    """
    Parameters: 
            user_name    = string of user name
            top_x        = integer of how many recommendations to return
            animal_type = specify cat or dog
    Output: 
            top X recommendations in list form"""
    # example of query - didn't end up using it
    #rankings_response=dynamo.query(
    #    TableName = table_name,
    #    KeyConditionExpression="user_id = :id",
    #    FilterExpression="contains(#animal_type,:animal_type)",
    #    ExpressionAttributeValues={
    #        ":id":{"S":user_name},
    #        ":animal_type":{"S":animal_type},
    #    },
    #    ExpressionAttributeNames={
    #        "#animal_type":"record",
    #    },
        #Select="user_id"        
    #)
    if animal_type == 'cat':
        animal_ids=cat_ids
        animal_model=collab_v2_cats_model
    elif animal_type == 'dog':
        animal_ids=dog_ids
        animal_model=collab_v2_dogs_model

    # Get reccs
    eligible_animals=animal_ids
    eligible_animals['Estimate_Score'] = eligible_animals['id'].apply(lambda x: animal_model.predict(user_name, x).est)
    eligible_animals = eligible_animals.sort_values('Estimate_Score', ascending=False) #best score first
    reccs= eligible_animals.head(top_x+10)['id'].tolist()

    # Query rankings dynamo table to check for already ranked pets
    # build the keys
    keys : List[Dict] = [
            { 'user_id': {'S': str(user_name)}, 'pet_id': {'S': str(pet_id)} } for pet_id in reccs
        ]
    # query
    table_name = "Rankings"
    response=dynamo.batch_get_item(
        RequestItems={
            table_name: {
                'Keys': keys
            }
        }   
    )

    collab_animals_check : List = response['Responses'][table_name] #put response in list
 
    for indx,_record in enumerate(collab_animals_check):
        
        collab_animals_check[indx].update(
            {'record': json.loads(collab_animals_check[indx]['record']['S'])}
        )

    animals_toremove = [animal['pet_id'] for animal in collab_animals_check]
    test_remove=[]
    for x in animals_toremove: #remove strings and make ids an int for comparision
        the_id= x['S']
        test_remove.append(int(the_id))

    animals_toremove = test_remove # animals to remove
    # Now that we have the removable animals, lets remove them from our reccs
    final_reccs = [i for i in reccs if i not in animals_toremove]
    if len(final_reccs) > top_x: # if more than top_X, cap it
        final_reccs =final_reccs[0:top_x]
    
    return final_reccs


#@app.post("/predict_content")
def predict_content(animal_id,top_x,animal_type: AnimalTypeEnum):
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
    if animal_type == 'cat':
        animal_model = content_v2_cats_model
    elif animal_type =='dog':
        animal_model = content_v2_dogs_model

    animal_id = int(animal_id) #guarantee an int or it will fail if not int
    reccs = animal_model[animal_id][:top_x]   
    reccstoOutput = []
    for rec in reccs: 
        reccstoOutput.append(int(rec[1]))

    return reccstoOutput


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086)