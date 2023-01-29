import streamlit as st
import re 


regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

def is_valid(email):
    """ validates user emails """
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def get_prefs():

    # set email as blank
    st.session_state['email'] = ''

    # set default values
    dog_size  = None
    dog_energy = None   
    dog_breed = None
    cat_size = None
    cat_energy = None
    cat_breed = None
    current_pets = None

    # present a form 
    with st.form("Let's get to know you and start looking for your new best friend!"):

        user_prefs = {}

        # text input
        full_name = st.text_input("What's your full name?")

        session_email = st.session_state['email']
        email = st.text_input("What's your email?",placeholder='Jax Doe')
        zip_code = st.number_input("Whats your zip code?",max_value=99999,min_value=00000)
        readiness = st.radio("How ready are you to adopt?",("Not ready","Somewhat ready","Very ready","Just curious"))
        age = st.number_input("How old are you?",max_value=120,min_value=4)
        if age < 4:
            st.error('Sorry, you must be at least 4 years old to use Petmatch Playground. Please call your parent')
            st.stop()
        g_expression = st.radio("How do you identify?",("M","F","Other","NA"))
        has_current_pets = st.radio("Do you currently have any pets?",("Yes","No"))
        if has_current_pets == "Yes":
            current_pets = st.radio("Do you have cat(s) or dog(s)?",("Cat(s)","Dog(s)","Both","Other Animal(s)"))

        # text input
        pet_type = st.radio("What type of pet are you looking for?",("Dog","Cat"))

        if pet_type == "Dog":
            dog_size = st.radio("What size of dog are you looking for?",("Small","Medium","Large"))
            dog_energy = st.radio("What level of energy are you looking for?",("Low","Medium","High"))
            dog_breed = st.radio("What breed(s) are you looking for?",("Mixed Breed","Pit Bull","Husky","Labrador","Golden Retriever","Other"))
        
        if pet_type == "Cat":
            cat_size = st.radio("What size of cat are you looking for?",("Small","Medium","Large")) 
            cat_energy = st.radio("What level of energy are you looking for?",("Low","Medium","High"))
            cat_breed = st.radio("What breed(s) are you looking for?",("Mixed Breed","Siamese","Persian","Maine Coon","Ragdoll"))
        
        preferences: list = st.multiselect(
            "Select which of these apply to your ideal pet:",
            [
        'Spayed or Neutered',
        'House Trained',
        'Has claws (Cats)',
        'Declawed (Cats)',
        'I would care for an animal with special needs',
        'Has its shots',
        'Good with kids'
        'Good with other animals',
        'Bonded Pairs',
        'Senior',
        'Youth',
        'Adolescent',
        'OK with an animal in recovery',
        'Quiet',
        'Talkative'
            ]
        )

        

        # TODO validate emails
        email_valid = is_valid(email)
        # if not email_valid:
        #     st.error('Email invalid. Enter a valid email.')
        # else:
        #     st.success('Valid email')
        form_sub = st.form_submit_button("Submit")

        user_prefs.update(
            {
            # conditionally add the animal pref 
            'dog_size': dog_size if dog_size else None,
            'dog_energy': dog_energy if dog_energy else None,
            'dog_breed': dog_breed if dog_breed else None,
            'cat_size': cat_size if cat_size else None,
            'cat_energy': cat_energy if cat_energy else None,
            'cat_breed': cat_breed if cat_breed else None,
            }
        )

        # add other preferences from the multi-select
        # for _indx,v in enumerate(preferences):
        #     if v == None:
        #         continue
        #     else:
        #         user_prefs.update(
        #             {v: True} 
        #         )
        user_prefs.update(
            {'user_prefs' : preferences}
        )

        user_prefs.update(
            {
                'full_name': full_name,
                'email': email,
                'zip_code': zip_code,
                'readiness': readiness,
                'age': age,
                'g_expression': g_expression,
                'has_current_pets': has_current_pets,
                'current_pets': current_pets           
            }
        )

        st.session_state['user_preferences'] = user_prefs

    return user_prefs
    







