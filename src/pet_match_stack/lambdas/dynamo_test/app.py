import json
import boto3

print('creating client')
client = boto3.client(
    'dynamodb', 
    # endpoint_url="http://9.9.9.9:8000",
    endpoint_url="http://localhost:8000",
    aws_access_key_id='dummyid',
    aws_secret_access_key='dummykey',
    aws_session_token='dummytoken',
    region_name='us-west-2'
    )

def lambda_handler(event, context):
    """ 
        Sample lambda function to connect to local dynamo db
    """
    try:
    #     dynamodb = boto3.resource('dynamodb', endpoint_url="http://9.9.9.9:8000")

        table_name = 'users_table'

        response = client.describe_table(TableName=table_name)
        
        print(response)
        item = "test"

    except Exception as e:
        raise e

    else:

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"{item}"
            }),
        }