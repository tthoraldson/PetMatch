import streamlit as st
import pandas as pd

# Intro page to PetMatch App

st.set_page_config(
    page_title="Petmatch Playground",
    page_icon="👋"
)

def intro():
    """
        This function operates the introduction page of PetMatch Streamlit app
    """


    # set title and description
    st.title('PetMatch Playground')

    st.write("# Welcome to PetMatch Playground 👋")
    st.sidebar.success("Select Dogs or Cats")

    st.markdown(
        """ 
        ## About PetMatch Playground
        PetMatch Playground is a web application that allows users to explore the PetMatch dataset and build a personalized pet recommendation system.
        """
    )

    user = st.selectbox(label='Select a user', options=['Theresa', 'Denise', 'Matt', 'Zsofi', 'Tibor', 'Klari'])

    return 'intro was run'

intro()
    
