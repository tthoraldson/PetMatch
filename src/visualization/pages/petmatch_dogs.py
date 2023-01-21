import streamlit as st
import pandas as pd
import os 

class DogsPetmatch:

    # TODO do not hardcode path to load dogs data
    dogs_path = '/app/data/version0_5/Adoptable_dogs_20221202_withExtras.csv'
    saveFile = '/app/rankings/petmatch_rankings_dogs.csv'

    def __init__(self):
        self.preferences = pd.DataFrame(columns=['user_name', 'dog_id', 'preference'])
        self.animal_type = 'dogs'
        self.sample_dogs = None
        self.display_name = None
        self.display_image = None
        self.display_description = None
        self.current_dog = None 
        self.user = None

    @st.cache
    def get_dog_data(self):

        dogs_path = self.dogs_path

        sample_dogs = pd.read_csv(self.dogs_path, low_memory=False)

        return f'retrieved dog data from {dogs_path}'

    def new_dog(self):
        # get sample dogs from saved session
        sample_dogs=st.session_state.sample_dogs
        # set session state variables
        self.current_dog = sample_dogs.sample()
        current_dog = self.current_dog
        
        # set instance attributes
        self.display_name = current_dog['name'].values[0]
        self.display_description = str(current_dog['description_x'].values)
        self.display_image= self.find_photo(current_dog).values

        self.env_children = str(current_dog['environment.children'].values)
        self.env_dogs = str(current_dog['environment.dogs'].values)
        self.env_cats  = str(current_dog['environment.cats'].values)
        self.house_trained = str(current_dog['attributes.house_trained'].values)
        self.special_needs = str(current_dog['attributes.special_needs'].values)
        self.breed_group = str(current_dog['group'].values)
        self.groom_freq = str(current_dog['grooming_frequency_category'].values)
        self.shed_freq = str(current_dog['shedding_category'].values)
        self.energy_type = str(current_dog['energy_level_category'].values)
        self.train_type = str(current_dog['trainability_category'].values)
        self.demeanor = str(current_dog['demeanor_category'].values)
        self.breed = str(current_dog['breeds.primary'].values)
        
        # update session state variables from instance attribuets
        st.session_state.current_dog = self.current_dog
        st.session_state.display_name = self.display_name
        st.session_state.display_description = self.display_description
        st.session_state.display_image = self.display_image
        st.session_state.env_children = self.env_children
        st.session_state.env_dogs = self.env_dogs
        st.session_state.env_cats = self.env_cats
        st.session_state.house_trained = self.house_trained
        st.session_state.special_needs = self.special_needs
        st.session_state.breed_group = self.breed_group
        st.session_state.groom_freq = self.groom_freq
        st.session_state.shed_freq = self.shed_freq
        st.session_state.energy_type = self.energy_type
        st.session_state.train_type = self.train_type
        st.session_state.demeanor = self.demeanor
        st.session_state.breed = self.breed

    # registers a disliked dog
    def disliked(self,current_dog):

        # get fileSave from instance
        filetoSave=self.saveFile

        
        updateRow= pd.concat([self.preferences, pd.DataFrame({'user_name': self.user, 'dog_id': current_dog['id'], 'preference': 0})], ignore_index=True)
        print('disliked...calling new dog ')
        
        self.appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
        self.new_dog()

    # registers a liked dog 
    def liked(self,current_dog):
        
        # get fileSave from instance
        filetoSave=self.saveFile
        
        updateRow = pd.concat([self.preferences, pd.DataFrame({'user_name': self.user, 'dog_id': current_dog['id'], 'preference': 1})], ignore_index=True)
        
        print('liked... calling ne dog')
        self.appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
        self.new_dog()

    def find_photo(self,current_dog):

        print(f"\n finding photos for current dog {current_dog} \n ")
        
        if not current_dog['photos'].empty:
            return current_dog['primary_photo_cropped.full']

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
    def initial_setup(self):

        # set the username from session state
        self.user = st.session_state.user

        saveFile = './rankings/petmatch_rankings_dogs.csv'
        sample_dogs = pd.read_csv(self.dogs_path, low_memory=False,header=0,index_col=0)
        
        # drop NAs 
        sample_dogs = sample_dogs.dropna(subset=['primary_photo_cropped.full'])

        # assign clean sample dogs dataframe
        self.sample_dogs = sample_dogs

        self.preferences = pd.DataFrame(columns=['user_name', 'dog_id', 'preference'])

        if not os.path.isfile(saveFile):
            self.appendDFToCSV_void(preferences,saveFile) # make file from scratch if it doesn't already exist
        if 'sample_dogs' not in st.session_state:
            st.session_state.sample_dogs=sample_dogs
        if 'saveFile' not in st.session_state:
            st.session_state.saveFile=saveFile
        if 'preferences' not in st.session_state:
            st.session_state.preferences=self.preferences

        # initialize session state for key dog instance variables if they don't already exist
        self.current_dog = self.sample_dogs.sample()

        self.display_name = self.current_dog['name'].values[0]
        self.display_description = str(self.current_dog['description_x'].values)
        self.display_image= self.find_photo(self.current_dog).values
        self.env_children = str(self.current_dog['environment.children'].values)
        self.env_dogs = str(self.current_dog['environment.dogs'].values)
        self.env_cats  = str(self.current_dog['environment.cats'].values)
        self.house_trained = str(self.current_dog['attributes.house_trained'].values)
        self.special_needs = str(self.current_dog['attributes.special_needs'].values)
        self.breed_group = str(self.current_dog['group'].values)
        self.groom_freq = str(self.current_dog['grooming_frequency_category'].values)
        self.shed_freq = str(self.current_dog['shedding_category'].values)
        self.energy_type = str(self.current_dog['energy_level_category'].values)
        self.train_type = str(self.current_dog['trainability_category'].values)
        self.demeanor = str(self.current_dog['demeanor_category'].values)
        self.breed = str(self.current_dog['breeds.primary'].values)

        # set session state from instance attributes
        if 'display_name' not in st.session_state:

            st.session_state.display_name = self.display_name
        if 'display_description' not in st.session_state:

            st.session_state.display_description = self.display_description
        if 'display_image' not in st.session_state:

            st.session_state.display_image = self.display_image
        if 'current_dog' not in st.session_state:

            st.session_state.current_dog = self.current_dog
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
        if 'breed_group' not in st.session_state:

            st.session_state.breed_group = self.breed_group
        if 'groom_freq' not in st.session_state:

            st.session_state.groom_freq = self.groom_freq
        if 'shed_freq' not in st.session_state:

            st.session_state.shed_freq = self.shed_freq
        if 'energy_type' not in st.session_state:

            st.session_state.energy_type = self.energy_type
        if 'train_type' not in st.session_state:

            st.session_state.train_type = self.train_type
        if 'demeanor' not in st.session_state:

            st.session_state.demeanor = self.demeanor
        if 'breed' not in st.session_state:

            st.session_state.breed = self.breed



# ==============================================================================

dogs_petmatch = DogsPetmatch()

if st.session_state['user'] is '':
    st.error(
        f"""Sorry, please click petmatch-start and enter your name to start the app.
        """
    )
    st.stop()

dogs_petmatch.initial_setup()

# set display attribuets from instance attributes
display_name = dogs_petmatch.display_name
display_description = dogs_petmatch.display_description
display_image = dogs_petmatch.display_image
current_dog = dogs_petmatch.current_dog
env_children = dogs_petmatch.env_children
env_dogs = dogs_petmatch.env_dogs
env_cats  = dogs_petmatch.env_cats
house_trained = dogs_petmatch.house_trained
special_needs = dogs_petmatch.special_needs
breed_group = dogs_petmatch.breed_group
groom_freq = dogs_petmatch.groom_freq
shed_freq = dogs_petmatch.shed_freq
energy_type = dogs_petmatch.energy_type
train_type = dogs_petmatch.train_type
demeanor = dogs_petmatch.demeanor
breed = dogs_petmatch.breed



# st.image('https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/58980756/6/?bust=1669602382&width=600')
st.title('PetMatch Playground')

# photo
if display_image is not None:
    st.image(display_image[0])
    

# header, description
st.header(display_name)
st.write(display_description)
print(display_description[0])

# add the expander
with st.expander("See more details about this animal"):
    #add stuff to help people choose
    st.write("Good with Children:", env_children)
    st.write("Good with Dogs:", env_dogs)
    st.write("Good with Cats:", env_cats)
    st.write("House Trained:",house_trained)
    st.write("Special Needs:",special_needs)
    st.write("Breed:",breed)
    st.write("AKC Breed Group:",breed_group)
    st.write("Grooming Frequency:",groom_freq)
    st.write("Shedding Frequency:",shed_freq)
    st.write("Energy Levels:",energy_type)
    st.write("Trainability:",train_type)
    st.write("General Breed Demeanor:",demeanor)

# add like buttons
col1, col2 = st.columns([1,1])
with col1:
    if st.button('Not For Me'):
        dogs_petmatch.disliked(
            current_dog
            ) 
        
with col2:
    if st.button('Like'):
        dogs_petmatch.liked(
            current_dog
            ) 
