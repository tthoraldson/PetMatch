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

table_name = 'users_table'

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

@app.get("/petmatch/")
def petmatch():

    # define the data to be inserted into the table
    data = {
        "userId": {
            "N": "2"
        },
        "name": {
            "S": "Test Doe"
        },
        "email": {
            "S": "johndoe@example.com"
        }
    }

    # insert the data into the table
    response = dynamo.put_item(TableName=table_name, Item=data)

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
                'user_id': {'S': str(uuid.uuid4())},
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086)