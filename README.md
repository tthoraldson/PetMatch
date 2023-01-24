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

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
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
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

--------
**Project Pitch Slides:** /reports/PetMatch_presentationSlides_20230123.pdf  
**Project Software Architecture Diagram:** /reports/figures/PetMatch_SystemDiagram_20230123.png  

**Still Need to Build:**  
* Collaborative Filtering v2 Cats  
* Collaborative Filtering v1 Dogs  
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
