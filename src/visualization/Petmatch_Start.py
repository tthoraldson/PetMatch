import streamlit as st
import pandas as pd
import get_user_prefs
import requests
import json

# Intro page to PetMatch App

st.set_page_config(
    page_title="Petmatch Playground",
    page_icon="👋"
)

def intro():
    """
        This function operates the introduction page of PetMatch Streamlit app
    """
    st.session_state['user_preferences'] = {}

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

    # store visibility in session state
    if 'visibility' not in st.session_state:
        st.session_state.disabled = False
        st.session_state.name_entered = False
    
    if st.session_state.disabled == False:    
        # allow user to enter a string name
        # TODO profanity-filter
        user : str = st.text_input(
            label='Enter a username 20 char max.', 
            max_chars=20,
            placeholder='Sam Placeholder',
            disabled=st.session_state.disabled
        )
        
        if not user:
            st.stop()
        else:
            # set session user in state
            st.session_state['user'] = user

            if st.session_state['user'] != '':
                st.success(f"Welcome {user}. We hope you find your new best friend!")
                
                # run the user data collection for preferences and pet recommendations
                get_user_prefs.get_prefs()

                st.write('You selected:',st.session_state['user_preferences'])

                # store user preferences in dynamodb 
                url = "http://fastapi:8086/petmatch/put_preferences/"
                json_data = json.dumps(st.session_state['user_preferences'])
                st.write(json_data)
                response = requests.post(url, data=json_data)
                st.write(f"API Request status: {response.status_code} {response.reason} {response.text}")

                
    return 'intro was run'

intro()
    
