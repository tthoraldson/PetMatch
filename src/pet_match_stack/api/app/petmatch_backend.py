import uvicorn
from fastapi import FastAPI
import boto3
from botocore.config import Config
import requests
import json

# configure boto3
my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

app = FastAPI()

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
            "N": "1"
        },
        "name": {
            "S": "John Doe"
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086)