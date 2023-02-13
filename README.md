PetMatch
==============================

Petmatch seeks to provide users with curated rescue animal recommendations in the hope that it will 
lead to higher adoptions rates and lower return rates to shelters. This will be accomplished through
the use of a recommendation model that extends an existing model in order to include no-kill shelters.
We will also build a serverless full-stack pipeline and a Tinder-like UI that matches adoptable pets
with potential adopters.

Team
------------
* Denise Blady  
* Theresa Thoraldson  
* Matthew Robinson  

Local Docker
------------
- To run all required containers locally
  - pull down `master` branch
  - run `BASE_PATH='<Path to this repo!>' docker compose up`
  - For example: `BASE_PATH='/Users/theresa/Desktop/source/PetMatch' docker compose up`
  - Alternative: Create a `.env` file at the root of the repository which contains an environment variable `BASE_PATH` and a string value leading the repository's root within your local file system.


Run Petmatch Docker
------------
- From the root of repository, run `docker-compose up`
- Troubleshooting - `docker-compose up --build --force-recreate -d` or `BASE_PATH='YOUR BASE PATH' docker compose up`

Prerequisites
------------
- Docker
- Docker Compose
- Python3.8>=
- Port Access Availability on local ports: 8086, 8001, 8002, 8003, 3000, 8501, 8087

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── rankings       <- User rankings (likes,dislikes)
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           
    |   |   └── dynamo     <- Local shared Dynamodb
    |   |   └── shared-local-instance.db <- Request this file from PetMatch team member
    |   ├── frontend       <- React and AWS Amplify code, frontend Dockerfile
    |   ├── pet_match_stack
    |   |   └── api        <- 
    |   |   |   └── app    <- FastAPI application code for main backend routes
    |   |   |   └── model_api <- FastAPI application code for ML models interactions routes
    |   |   |   └── fastapi.Dockerfile <- FastAPI application Dockerfile
    |   |   |
    |   |   └── db-setup <- DynamoDB local setup scripts and Dockerfile
    |   |   └── infra    <- Terraform infrastructure
    |   |   └── lambdas  <- AWS Lambda code 
    |   |   └── tests    <- Testing sweet
    |   | 
    │   └── visualization  <- Contains scripts and Dockerfiles to run the Petmatch Streamlit application this contains basic version of Petmatch
    |       └── pages <- Streamlit multi-page app pages
    |       └── rankings <- Destination for saved user Rankings (likes of animals)
    |       └── get_user_prefs.py <- script to collect user preferences
    |       └── Petmatch_Start.py <- Streamlit application homepage 
    │
    └── docker-compose.yml   <- Docker Compose configuration that sets up and configures your local stack

--------
**Project Pitch Slides:** /reports/PetMatch_presentationSlides_20230123.pdf  
**Project Software Architecture Diagram:** /reports/figures/PetMatch_SystemDiagram_20230123.png  

**Still Need to Build:**  
* Incorporate best content-based filtering model for cats and dogs into MLE Stack  
* Incorporate best collaborative filtering model for cats and dogs into MLE Stack  
* Finish setting up deployment stack  
* UI upgrades deployment (user cold-start preferences, etc..)    

**Future Work:**  
* Continue collecting user rankings  
* Add timestamp to user rankings for time-sensitive recommendations  
* Incorporate distance more effectively into models  
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
