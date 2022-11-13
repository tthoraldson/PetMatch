# import modules path
import sys
sys.path.append("./lib/")
from lib import requests # TODO smoother imports with layers
import json
import os

# petfinder environment vars
from lib import dotenv
from dotenv import dotenv_values

env_vars = { 
        **dotenv_values(".env.secret"), 
        **dotenv_values(".env.shared")
    }

PETFINDER_API_URL = env_vars.get("PETFINDER_API_URL")
GRANT_TYPE=env_vars.get("GRANT_TYPE")
CLIENT_ID=env_vars.get("PETFINDER_API_KEY")
CLIENT_SECRET=env_vars.get("PETFINDER_SECRET")


def lambda_handler(event, context):
    """
        Sample lambda function to connect to PetFinder API
    """

    try:
        print(f"POST'ing to URL:{PETFINDER_API_URL}")
        # send authentication
        res = requests.post(
            PETFINDER_API_URL,
            data={
                    'grant_type': GRANT_TYPE,
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET
                }
            )

        # get response
        response = json.loads(res.text)

        # parse token info and expiration (3600 or one hour)
        access_token = response['access_token']
    
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{response}",
            # "location": ip.text.replace("\n", "")
        }),
    }
