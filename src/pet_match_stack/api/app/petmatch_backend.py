import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import boto3
from botocore.config import Config
import requests
import json
import uuid
from typing import Union, Optional
import datetime

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

class Ranking(BaseModel):
    user_id : str
    pet_id : str
    response : bool

@app.post("/petmatch/put_ranking")
def petmatch_put_ranking(ranking:Ranking):

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


# TODO fix params
@app.post("/get_url")
async def get_url(animal_id ,animals_df ):
    """
    Parameters: 
            animal_id  = animal id
            animals_df = dataframe of all animals of chosen type (dog, cat) 
    Output: 
            petfinder url of given animal_id
    """
    
    ds = animals_df
    colsGrab = ['url']

    return ds.loc[ds['id'] == animal_id][colsGrab].values[0]    



# TODO fix params
@app.post("/get_picture")
async def get_picture(animal_id,animals_df):  
    """
    Parameters: 
            animal_id  = animal id
            animals_df = dataframe of all animals of chosen type (dog, cat) 
    Output: 
            petfinder url of given animal_id
    """
    ds = animals_df
    colsGrab = ['primary_photo_cropped.full']
    return ds.loc[ds['id'] == animal_id][colsGrab].values[0]



# TODO fix params
@app.post("/predict_collab")
async def predict_collab(pet_rankings,user_name,top_x,animal_model):
    """
    Parameters: 
            pet_rankings = dataframe of all pet rankings of the chosen animal type
            user_name    = string of user name
            top_x        = integer of how many recommendations to return
            animal_model = pre-trained model to make recommendations with
    Output: 
            top X recommendations in list form"""

    all_1user_rankings = pet_rankings[pet_rankings['user_name'] == user_name]
    rankings_minusKnownbyUser = pd.concat([pet_rankings,all_1user_rankings], axis=0, ignore_index=True).drop_duplicates(subset=["user_name","animal_id"],keep=False, ignore_index=True) # only remove user specific rankings from overall list, not everyone's!
    eligible_animals = rankings_minusKnownbyUser[['animal_id']]
    eligible_animals['Estimate_Score'] = eligible_animals['animal_id'].apply(lambda x: animal_model.predict(user_name, x).est)
    eligible_animals = eligible_animals.sort_values('Estimate_Score', ascending=False)
    #print(eligible_animals.head(top_x)) # get top X reccs
    reccs= eligible_animals.head(top_x)['animal_id'].tolist()
    return reccs



def get_item_id(animal_id,animals_df):  
    """
    required by predict_content
    This method is required to translate from content-based model id for that animal and the petfinder data for that animal. 
    This ensures the correct petfinder data for the animal is retrieved and is a safety measure
    Parameters: 
            animal_id  = animal id
            animals_df = dataframe of all animals of chosen type (dog, cat) 
    Output: 
            petfinder id of animal from content-based recommender
    """
    ds = animals_df
    colsGrab = ['id']
    return ds.loc[ds['id'] == animal_id][colsGrab].values[0]

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