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
cats_path = 'app/data/version0_5/Adoptable_cats_20221125.csv'
dogs_master_path = 'app/data/version0_5/Adoptable_dogs_20221202_withExtras.csv'
dogs_contentbased_path = 'app/data/version0_5/dogsAdoptablewithExtrasv2.csv'
rankings_path = 'app/data/rankings/petmatch_rankings.csv'

# Create JSON -> Dics and List of Dics (json required for backend processing by dynamo)
catsAdoptable_json= json.loads(
    pd.read_csv(cats_path,low_memory=False).dropna(subset=['primary_photo_cropped.full'])
    .to_json(orient='records')
)
dogsAdoptable_master_json= json.loads(
    pd.read_csv(dogs_master_path,low_memory=False).dropna(subset=['primary_photo_cropped.full'])
    .to_json(orient='records')
)
dogsAdoptable_contentbased_json= json.loads(
    pd.read_csv(dogs_contentbased_path,low_memory=False).dropna(subset=['primary_photo_cropped.full'])
    .to_json(orient='records')
)
rankings_json= json.loads(
    pd.read_csv(rankings_path,low_memory=False)
    .to_json(orient='records')
)

# Create a list of dictionaries and their table name
lst_Dics = [{'item':rankings_json,'table':'Rankings'}]#,
            #{'item':catsAdoptable_json,'table':'Cats-Adoptable'},
            #{'item':dogsAdoptable_master_json,'table':'Dogs-Adoptable-master'},
            #{'item':dogsAdoptable_contentbased_json,'table':'Dogs-Adoptable-contentbased'}]

#Connect to DynamoDb Function
def insertDynamoItem(table_name,item_lst):
    
    for record in item_lst:
        dynamo.put_item(
            TableName=f'{table_name}',
            Item={
                'pet_id': {'S': str(record['id'])} ,
                'animal_id': {'S': str(record['id'])}, 
                'record': {'S':json.dumps(record)}
                }
            )

    print('Success-Initial DB population',table_name,sep=" ")

# Upload Content to DynamoDB
for element in lst_Dics:
    insertDynamoItem(element['table'],element['item'])