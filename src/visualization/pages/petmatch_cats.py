import time
import streamlit as st
import pandas as pd
import os 

class CatsPetmatch:

    # TODO do not hardcode path to load cats data
    cats_path = '/app/data/version0_5/Adoptable_cats_20221125.csv'
    saveFile = '/app/rankings/petmatch_rankings_cats.csv'

    # instance attrs
    def __init__(self):
        self.preferences = pd.DataFrame(columns=['user_name', 'cat_id', 'preference'])
        self.animal_type = 'cats'
        self.sample_cats = None
        self.display_name = None
        self.display_image = None
        self.display_description = None
        self.current_cat = None
        self.user = None 

    # use a cache decorator to optimize retrieval of pet data
    @st.cache
    def get_cat_data(self):

        # cats path is same for all class instances
        cats_path = self.cats_path

        sample_cats = pd.read_csv(self.cats_path, low_memory=False)

        # set sample cats data for the instance
        self.sample_cats = sample_cats.dropna(subset=['primary_photo_cropped.full'])

        return f'retrieved cat data from {cats_path}'

    # gets a new cat to display
    def new_cat(self):
        
        # set a new sample cat as instance's current cats
        self.current_cat = self.sample_cats.sample()

        # rename to current cat
        current_cat = self.current_cat

        self.display_name = current_cat['name'].values[0]
        self.display_description = current_cat['description']

        self.display_image = self.find_photo(current_cat)

        # set session state variables
        self.env_children = str(current_cat['environment.children'].values)
        self.env_dogs = str(current_cat['environment.dogs'].values)
        self.env_cats  = str(current_cat['environment.cats'].values)
        self.house_trained = str(current_cat['attributes.house_trained'].values)
        self.special_needs = str(current_cat['attributes.special_needs'].values)

        # update session state variables
        st.session_state.current_cat = self.current_cat
        st.session_state.display_name = self.display_name
        st.session_state.display_description = self.display_description
        st.session_state.display_image = self.display_image
        st.session_state.env_children = self.env_children
        st.session_state.env_dogs = self.env_dogs
        st.session_state.env_cats = self.env_cats
        st.session_state.house_trained = self.house_trained
        st.session_state.special_needs = self.special_needs

    # registers a disliked cat
    def disliked(self,current_cat):

        # get fileSave from saved session
        filetoSave = self.saveFile
        
        # get preferences frame from saved session
        # self.preferences=st.session_state.preferences
        
        updateRow= pd.concat([self.preferences, pd.DataFrame({'user_name': self.user, 'cat_id': current_cat['id'], 'preference': 0})], ignore_index=True)
        print('disliked... calling new cat')
        
        self.appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
        self.new_cat()

    # registers a liked cat
    def liked(self,current_cat):
        
        filetoSave = self.saveFile

        print('liked calling new cat...')
        updateRow= pd.concat([self.preferences, pd.DataFrame({'user_name': self.user, 'cat_id': current_cat['id'], 'preference': 1})], ignore_index=True)
        
        
        self.appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
        
        self.new_cat()
        

    # find cat photo(s)
    def find_photo(self, current_cat):

        print(f"\n finding photos for current cat {current_cat} \n ")
        
        if not current_cat['photos'].empty:


            return current_cat['primary_photo_cropped.full']

    def appendDFToCSV_void(self, df, csvFilePath, sep=","):
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

    # @st.experimental_memo(suppress_st_warning=True)
    # def initialize_state(_self):



    # @st.experimental_memo(suppress_st_warning=True)
    def initial_setup(self): # tell streamlit not to hash the parameter with an underscore

        # set the username from session state
        self.user = st.session_state.user

        saveFile = './rankings/petmatch_rankings_cats.csv' # TODO update this path
        
        sample_cats = pd.read_csv(self.cats_path, low_memory=False,header=0,index_col=0)
        
        sample_cats = sample_cats.dropna(subset=['primary_photo_cropped.full'])
        

        # assign clean sample cats dataframe
        self.sample_cats = sample_cats

        self.preferences = pd.DataFrame(columns=['user_name', 'cat_id', 'preference'])
        if not os.path.isfile(saveFile):
            self.appendDFToCSV_void(self.preferences,saveFile) # make file from scratch if it doesn't already exist
        if 'sample_cats' not in st.session_state:
            st.session_state.sample_cats=sample_cats
        if 'saveFile' not in st.session_state:
            st.session_state.saveFile=saveFile
        if 'preferences' not in st.session_state:
            st.session_state.preferences=self.preferences

        # initialize session state for key cat instance variables if they don't already exist
        self.current_cat = self.sample_cats.sample()

        self.display_name = self.current_cat['name'].values[0]
        self.display_description = str(self.current_cat['description'].values)
        self.display_image = self.find_photo(self.current_cat).values
        self.env_children = str(self.current_cat['environment.children'].values)
        self.env_dogs = str(self.current_cat['environment.dogs'].values)
        self.env_cats  = str(self.current_cat['environment.cats'].values)
        self.house_trained = str(self.current_cat['attributes.house_trained'].values)
        self.special_needs = str(self.current_cat['attributes.special_needs'].values)

        # set session state from instance attributes
        if 'display_name' not in st.session_state:
            
            st.session_state.display_name = self.display_name
        if 'display_description' not in st.session_state:
            
            st.session_state.display_description = self.display_description
        if 'display_image' not in st.session_state:
            
            st.session_state.display_image = self.display_image
        if 'current_cat' not in st.session_state:
            
            st.session_state.current_cat = self.current_cat
        if 'env_children' not in st.session_state:
            
            st.session_state.env_children = self.env_children
        if 'env_dogs' not in st.session_state:
            
            st.session_state.env_dogs = self.env_dogs
        if 'env_cats' not in st.session_state:
            
            st.session_state.env_cats = self.env_cats
        if 'house_trained' not in st.session_state:
            
            st.session_state.house_trained = self.house_trained
        if 'special_needs' not in st.session_state:
            
            st.session_state.special_needs = self.special_needs


cats_petmatch = CatsPetmatch()

if st.session_state['user'] is '':
    st.error(
        f"""Sorry, please click 'Petmatch Start' and enter your name to start the app.
        """
    )
    st.stop()

# initial setup of cats
cats_petmatch.initial_setup()

# set display attributes from instance attributes

display_name = cats_petmatch.display_name
display_description = cats_petmatch.display_description
display_image = cats_petmatch.display_image
current_cat = cats_petmatch.current_cat
env_children = cats_petmatch.env_children
env_dogs = cats_petmatch.env_dogs
env_cats  = cats_petmatch.env_cats
house_trained = cats_petmatch.house_trained
special_needs = cats_petmatch.special_needs

# photo
if display_image is not None:
    print(display_image)

    st.image(display_image[0])

# header, description
st.header(cats_petmatch.display_name)
st.write(cats_petmatch.display_description)


# # add the expander
with st.expander("See more details about this animal"):
    #add stuff to help people choose
    st.write("Good with Children:", env_children)
    st.write("Good with Dogs:", env_dogs)
    st.write("Good with Cats:", env_cats)
    st.write("House Trained:",house_trained)
    st.write("Special Needs:",special_needs)

# add like buttons
col1, col2 = st.columns([1,1])
with col1:
    if st.button('Not For Me'):
        cats_petmatch.disliked(
                cats_petmatch.current_cat
            )
with col2:
    if st.button('Like'):
        cats_petmatch.liked(
                cats_petmatch.current_cat
            )

# access saved values from session
# display_name=st.session_state.display_name
# display_description=st.session_state.display_description
# display_image=st.session_state.display_image
# current_cat=st.session_state.current_cat
# env_children = st.session_state.env_children
# env_dogs = st.session_state.env_dogs
# env_cats  = st.session_state.env_cats
# house_trained = st.session_state.house_trained
# special_needs = st.session_state.special_needs