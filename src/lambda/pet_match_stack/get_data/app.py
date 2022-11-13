# import modules path
import sys
sys.path.append("./lib/")
from lib import requests
import json

# TODO smoother imports with layers


def lambda_handler(event, context):
    """
        Sample lambda function to connect to PetFinder API
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello pets!!",
            # "location": ip.text.replace("\n", "")
        }),
    }
