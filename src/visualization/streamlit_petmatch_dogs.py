import streamlit as st
import pandas as pd
import os

def new_dog():
    # get sample dogs from saved session
    sample_dogs=st.session_state.sample_dogs
    # set session state variables
    current_dog = sample_dogs.sample()
    display_name = current_dog['name'].values[0]
    display_description = str(current_dog['description'])
    display_image= find_photo(current_dog).values
    # update session state variables
    st.session_state.current_dog = current_dog
    st.session_state.display_name = display_name
    st.session_state.display_description = display_description
    st.session_state.display_image = display_image

def disliked(current_dog):
    # get fileSave from saved session
    filetoSave=st.session_state.saveFile
    # get preferences frame from saved session
    preferences=st.session_state.preferences
    updateRow= pd.concat([preferences, pd.DataFrame({'user_name': user, 'dog_id': current_dog['id'], 'preference': 0})], ignore_index=True)
    print('disliked')
    appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
    new_dog()

def liked(current_dog):
    # get fileSave from saved session
    filetoSave=st.session_state.saveFile
    # get preferences frame from saved session
    preferences=st.session_state.preferences
    updateRow = pd.concat([preferences, pd.DataFrame({'user_name': user, 'dog_id': current_dog['id'], 'preference': 1})], ignore_index=True)
    print('liked')
    appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
    new_dog()

def find_photo(current_dog):
    print(vars(current_dog['photos']))
    if not current_dog['photos'].empty:
        return current_dog['primary_photo_cropped.full']

def appendDFToCSV_void(df, csvFilePath, sep=","):
    try:
        if not os.path.isfile(csvFilePath):
            print("creating file for first time")
            headers = df.columns
            df.to_csv(csvFilePath, mode='+a', index=False, sep=sep,header=headers)
        elif len(df.columns) != len(pd.read_csv(csvFilePath, nrows=1, sep=sep).columns):
            print("save nothing. Columns do not match")
            raise Exception("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(pd.read_csv(csvFilePath, nrows=1, sep=sep).columns)) + " columns.")
        elif not (df.columns == pd.read_csv(csvFilePath, nrows=1, sep=sep).columns).all():
            print("save nothing. Columns/column order do not match")
            raise Exception("Columns and column order of dataframe and csv file do not match!!")
        else:
            headers = df.columns
            print("write update")
            df.to_csv(csvFilePath, mode='+a', index=False, sep=sep,header=False)
    except PermissionError:
        pass

@st.experimental_memo(suppress_st_warning=True)
def initial_setup():
    saveFile = '../../data/rankings/petmatch_rankings_dogs.csv'
    sample_dogs = pd.read_csv('../../data/raw/version0_5/Adoptable_dogs_20221202.csv', low_memory=False,header=0,index_col=0)
    sample_dogs = sample_dogs.dropna(subset=['primary_photo_cropped.full'])
    preferences = pd.DataFrame(columns=['user_name', 'dog_id', 'preference'])
    if not os.path.isfile(saveFile):
        appendDFToCSV_void(preferences,saveFile) # make file from scratch if it doesn't already exist
    if 'sample_dogs' not in st.session_state:
        st.session_state.sample_dogs=sample_dogs
    if 'saveFile' not in st.session_state:
        st.session_state.saveFile=saveFile
    if 'preferences' not in st.session_state:
        st.session_state.preferences=preferences

    # initialize session state for key dog instance variables if they don't already exist
    current_dog = sample_dogs.sample()
    display_name = current_dog['name'].values[0]
    display_description = str(current_dog['description'])
    display_image= find_photo(current_dog).values
    if 'display_name' not in st.session_state:
        st.session_state.display_name=display_name
    if 'display_description' not in st.session_state:
        st.session_state.display_description=display_description
    if 'display_image' not in st.session_state:
        st.session_state.display_image=display_image
    if 'current_dog' not in st.session_state:
        st.session_state.current_dog=current_dog
    # set up actual first dog for user
    new_dog()


# ==============================================================================
initial_setup()
# access saved values from session
display_name=st.session_state.display_name
display_description=st.session_state.display_description
display_image=st.session_state.display_image
current_dog=st.session_state.current_dog
st.write(display_image[0])

# st.image('https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/58980756/6/?bust=1669602382&width=600')
st.title('PetMatch Playground')

if display_image is not None:
    st.image(display_image[0])


user = st.selectbox(label='Select a user', options=['Theresa', 'Denise', 'Matt'])

# photo
st.header(display_name)
st.write(display_description)


col1, col2 = st.columns([1,1])
with col1:
    if st.button('dislike'):
        disliked(current_dog) 
        st.experimental_rerun() # required so UI reflects current values
with col2:
    if st.button('like'):
        liked(current_dog) 
        st.experimental_rerun() # required so UI reflects current values
