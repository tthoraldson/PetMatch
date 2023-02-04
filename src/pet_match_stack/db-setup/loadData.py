#Import Libraries
import boto3
import pandas as pd
import json
from botocore.config import Config

#Set dynamo client, also set in backend, do I have to set it again?
# configure boto3
my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

dynamo = boto3.client(
        'dynamodb', 
        endpoint_url='http://dynamo:8001',
        config=my_config,
        aws_access_key_id='DUMMYIDEXAMPLE',
        aws_secret_access_key='DUMMYEXAMPLEKEY'
    )

# File paths for data
cats_path = '/app/data/version0_5/Adoptable_cats_20221125.csv'

# Create JSON -> Dics and List of Dics (json required for backend processing by dynamo)
catsAdoptable_json= json.loads(
    pd.read_csv(cats_path,low_memory=False).dropna(subset=['primary_photo_cropped.full'])
    .to_json(orient='records')
)
# TODO Add dogs once cats works

# Create a list of dictionaries and their table name
lst_Dics = [[{'item':catsAdoptable_json,'table':'Cats-Adoptable'}]]

#Connect to DynamoDb Function
def insertDynamoItem(tablename,item_lst):
    dynamoTable = dynamo.Table(tablename)
    for record in item_lst:
        dynamoTable.put_item(Item=record)

    print('Success-Initial DB population',tablename,sep=" ")

# Upload Content to DynamoDB
for element in lst_Dics:
    insertDynamoItem(element['table'],element['item'])