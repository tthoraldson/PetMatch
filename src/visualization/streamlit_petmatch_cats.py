import streamlit as st
import pandas as pd
import os

def new_cat():
    # get sample cats from saved session
    sample_cats=st.session_state.sample_cats
    # set session state variables
    current_cat = sample_cats.sample()
    display_name = current_cat['name'].values[0]
    display_description = str(current_cat['description'])
    display_image= find_photo(current_cat).values
    # update session state variables
    st.session_state.current_cat = current_cat
    st.session_state.display_name = display_name
    st.session_state.display_description = display_description
    st.session_state.display_image = display_image

def disliked(current_cat):
    # get fileSave from saved session
    filetoSave=st.session_state.saveFile
    # get preferences frame from saved session
    preferences=st.session_state.preferences
    updateRow= pd.concat([preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 0})], ignore_index=True)
    print('disliked')
    appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
    new_cat()

def liked(current_cat):
    # get fileSave from saved session
    filetoSave=st.session_state.saveFile
    # get preferences frame from saved session
    preferences=st.session_state.preferences
    updateRow = pd.concat([preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 1})], ignore_index=True)
    print('liked')
    appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
    new_cat()

def find_photo(current_cat):
    print(vars(current_cat['photos']))
    if not current_cat['photos'].empty:
        return current_cat['primary_photo_cropped.full']

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
    saveFile = '../../data/rankings/petmatch_rankings_cats.csv'
    sample_cats = pd.read_csv('../../data/raw/version0_5/Adoptable_cats_20221125.csv', low_memory=False,header=0,index_col=0)
    sample_cats = sample_cats.dropna(subset=['primary_photo_cropped.full'])
    preferences = pd.DataFrame(columns=['user_name', 'cat_id', 'preference'])
    if not os.path.isfile(saveFile):
        appendDFToCSV_void(preferences,saveFile) # make file from scratch if it doesn't already exist
    if 'sample_cats' not in st.session_state:
        st.session_state.sample_cats=sample_cats
    if 'saveFile' not in st.session_state:
        st.session_state.saveFile=saveFile
    if 'preferences' not in st.session_state:
        st.session_state.preferences=preferences

    # initialize session state for key cat instance variables if they don't already exist
    current_cat = sample_cats.sample()
    display_name = current_cat['name'].values[0]
    display_description = str(current_cat['description'])
    display_image= find_photo(current_cat).values
    if 'display_name' not in st.session_state:
        st.session_state.display_name=display_name
    if 'display_description' not in st.session_state:
        st.session_state.display_description=display_description
    if 'display_image' not in st.session_state:
        st.session_state.display_image=display_image
    if 'current_cat' not in st.session_state:
        st.session_state.current_cat=current_cat
    # set up actual first cat for user
    new_cat()


# ==============================================================================
initial_setup()
# access saved values from session
display_name=st.session_state.display_name
display_description=st.session_state.display_description
display_image=st.session_state.display_image
current_cat=st.session_state.current_cat
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
        disliked(current_cat) 
        st.experimental_rerun() # required so UI reflects current values
with col2:
    if st.button('like'):
        liked(current_cat) 
        st.experimental_rerun() # required so UI reflects current values
