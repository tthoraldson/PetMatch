from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any
from enum import Enum
import json
import requests

app = FastAPI()

# fastapi model
class PetMatchQuery(BaseModel):
    """PetMatch Query base model"""
    # use attrs to define restrictions on the values below
    type: str = Field( 
        description="Return results matching animal type",
        type=str,
        values="Possible values may be looked up via Get Animal Types. " 
        )   
    status: str = Field( 
        description="Return results matching adoption status",
        type=str,
        values="adoptable  adopted  found Accepts multiple values (default: adoptable)" 
        )   
    special_needs: bool = Field( 
        description="Return results that have special needs",
        type =bool,
        values="Can be true or 1 only"
        )   
    sort: str = Field( 
        description="Attribute to sort by; leading dash requests a reverse-order sort",
        type=str,
        values="recent  -recent  distance  -distance  random (default: recent)" 
        )   
    size: str = Field( 
        description="Return results matching animal size",
        type=str,
        values="small  medium  large  xlarge Accepts multiple values  e.g. size=large xlarge. " 
        )   
    page: int = Field( 
        description="Specifies which page of results to return",
        type=int,
        values="(default: 1) " 
        )   
    organization: str = Field( 
        description="Return results associated with specific organization(s)",
        type=str,
        values="Accepts multiple values  e.g. organization=[ID1] [ID2]." 
        )   
    name: str = Field( 
        description="Return results matching animal name (includes partial matches; e.g. 'Fred' will return 'Alfredo' and 'Frederick')",
        type=str,
        values="" 
        )   
    location: str = Field( 
        description="Return results by location.",
        type=str,
        values="city  state; latitude longitude; or postal code." 
        )   
    limit: int = Field( 
        description="Maximum number of results to return per 'page' response",
        type=int,
        values="(default: 20  max: 100) " 
        )   
    house_trained: bool = Field( 
        description="Return results that are house trained",
        type =bool,
        values="Can be true or 1 only "
        )   
    good_with_dogs : bool = Field(
        description="Return results that are good with dogs",
        type =bool,
        values="Can be true  false 1  or 0 "
        )   
    good_with_children: bool = Field(
        description="Return results that are good with children",
        type =bool,
        values="Can be true  false 1  or 0 "
        )   
    good_with_cats: bool = Field( 
        description="Return results that are good with cats",
        type =bool,
        values="Can be true  false 1  or 0 "
        )   
    gender: str = Field( 
        description="Return results matching animal gender",
        type=str,
        values="male  female  unknown Accepts multiple values  e.g. gender=male female. " 
        )   
    distance: int = Field( 
        description="Return results within distance of location (in miles).",
        type=int,
        values="Requires location to be set (default: 100  max: 500) " 
        )   
    declawed: bool = Field( 
        description="Return results that are declawed",
        type =bool,
        values="Can be true or 1 only "
        )   
    color: str = Field( 
        description="Return results matching animal color",
        type=str,
        values="Possible values may be looked up via Get Animal Types. " 
        )   
    coat: str = Field( 
        description="Return results matching animal coat",
        type=str,
        values="short  medium  long  wire  hairless  curly Accepts multiple values  e.g. coat=wire curly." 
        )   
    breed: str = Field( 
        description="Return results matching animal breed",
        type=str,
        values="Accepts multiple values  e.g. breed=pug samoyed. Possible values may be looked up via Get Animal Breeds below." 
        )   
    before: str = Field( 
        description="Return results published before this date/time.",
        type=str,
        values="Must be a valid ISO8601 date-time string (e.g. 2019-10-07T19:13:01+00:00) " 
        )   
    age: str = Field( 
        description="Return results matching animal age",
        type=str,
        values="baby  young  adult  senior Accepts multiple values  e.g. age=baby senior. " 
        )   
    after: str = Field( 
        description="Return results published after this date/time.",
        type=str,
        values="Must be a valid ISO8601 date-time string (e.g. 2019-10-07T19:13:01+00:00) " 
        )   
    




# create boiler plate api
@app.get("/")
def read_root():
    return {"Hello": "World"}

# post request to PETMATCH_API
@app.post("/petmatch/{params}")
# create a function to get data from petfinder api
def get_petmatch_data(
    PetMatchQuery: PetMatchQuery,
):

    # parse params into variables
    params = PetMatchQuery.dict()
    # print(params)
    
    
    # create a headers dictionary for the api request
    headers = {
        {'Authorization': f'Bearer' + PETMATCH_API}
    }
    # create a dictionary to store the data
    data = {
        'api_key': config.PETMATCH_API_KEY,
        'animal_type': 'dog',
        'breed': 'labrador',
        'age': 'adult',
        'size': 'medium',
    }

    # post request to PETMATCH_API
    response = requests.post(PETMATCH_API, data=data)

    # return the response body as json
    return response.json()