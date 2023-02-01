from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import boto3
from botocore.config import Config
import json
import uuid
# from surprise import Dataset, accuracy, SVDpp # if only non-model training probably only needs SVDpp
# from surprise.model_selection import cross_validate
# from surprise import Reader

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
    "http://localhost:8087"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.post("/retrain_collaborativeFiltering")
# async def retrain_collaborativeFiltering(trainingset_full):
#     """ 
#     Retrain Collaborative Filtering model
#     Parameters: 
#                 trainingset_full  = fully set up training data to fit
#     Output: 
#                 newly trained model
#     """

#     algoChosen= SVDpp(n_epochs=15,lr_all=0.01) #chosen algo
#     algoChosen.fit(trainingset_full)
#     #<TODO> save to model store in AWS
#     return algoChosen

# @app.post("/cross_validate_collaborativeFiltering")
# async def cross_validate_collaborativeFiltering(training_data,numFolds=10):
#     """    
#     Check performance of Collaborative Filtering model
#     Parameters: 
#             training_data  = training data to use
#             numFolds       = number of cross validation folds to use
#     Output: 
#             printed performance metrics for now...
#     """

#     algoChosen= SVDpp(n_epochs=15,lr_all=0.01) #chosen algo
#     print(cross_validate(algoChosen, training_data, measures=['RMSE', 'MAE'], cv=numFolds, verbose=True))

#     return



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8087)