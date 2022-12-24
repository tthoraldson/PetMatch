import streamlit as st
import pandas as pd
import os 

class DogsPetmatch:

    # TODO do not hardcode path to load dogs data
    dogs_path = '../../data/raw/version0_5/Adoptable_dogs_20221202_withExtras.csv'
    sample_dogs = pd.read_csv(dogs_path, low_memory=False,header=0,index_col=0)
    saveFile = '../../data/rankings/petmatch_rankings_dogs.csv'

    def __init__(self):
        self.preferences = pd.DataFrame(columns=['user_name', 'dog_id', 'preference'])
        self.animal_type = 'dogs'
        self.sample_dogs = None
        self.display_name = None
        self.display_image = None
        self.display_description = None
        self.current_dog = None
        self.user = 'Matt' # TODO change this to non-hardcoded

    def new_dog(self):
        # get sample dogs from saved session
        sample_dogs=st.session_state.sample_dogs
        # set session state variables
        self.current_dog = sample_dogs.sample()
        current_dog = self.current_dog
        
        display_name = current_dog['name'].values[0]
        display_description = str(current_dog['description_x'].values)
        display_image= self.find_photo(current_dog).values
        env_children = str(current_dog['environment.children'].values)
        env_dogs = str(current_dog['environment.dogs'].values)
        env_cats  = str(current_dog['environment.cats'].values)
        house_trained = str(current_dog['attributes.house_trained'].values)
        special_needs = str(current_dog['attributes.special_needs'].values)
        breed_group = str(current_dog['group'].values)
        groom_freq = str(current_dog['grooming_frequency_category'].values)
        shed_freq = str(current_dog['shedding_category'].values)
        energy_type = str(current_dog['energy_level_category'].values)
        train_type = str(current_dog['trainability_category'].values)
        demeanor = str(current_dog['demeanor_category'].values)
        breed = str(current_dog['breeds.primary'].values)
        # update session state variables
        st.session_state.current_dog = current_dog
        st.session_state.display_name = display_name
        st.session_state.display_description = display_description
        st.session_state.display_image = display_image
        st.session_state.env_children = env_children
        st.session_state.env_dogs = env_dogs
        st.session_state.env_cats = env_cats
        st.session_state.house_trained = house_trained
        st.session_state.special_needs = special_needs
        st.session_state.breed_group = breed_group
        st.session_state.groom_freq = groom_freq
        st.session_state.shed_freq = shed_freq
        st.session_state.energy_type = energy_type
        st.session_state.train_type = train_type
        st.session_state.demeanor = demeanor
        st.session_state.breed = breed

    def disliked(self,current_dog):
        # get fileSave from saved session
        filetoSave=st.session_state.saveFile
        # get preferences frame from saved session
        preferences=st.session_state.preferences
        updateRow= pd.concat([preferences, pd.DataFrame({'user_name': user, 'dog_id': current_dog['id'], 'preference': 0})], ignore_index=True)
        print('disliked')
        self.appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
        self.new_dog()

    def liked(self,current_dog):
        # get fileSave from saved session
        filetoSave=st.session_state.saveFile
        # get preferences frame from saved session
        preferences=st.session_state.preferences
        updateRow = pd.concat([preferences, pd.DataFrame({'user_name': user, 'dog_id': current_dog['id'], 'preference': 1})], ignore_index=True)
        print('liked')
        self.appendDFToCSV_void(updateRow,filetoSave) #save dataframe to csv in append mode
        self.new_dog()

    def find_photo(self,current_dog):
        print(vars(current_dog['photos']))
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

    @st.experimental_memo(suppress_st_warning=True)
    def initial_setup(self):
        saveFile = '../../data/rankings/petmatch_rankings_dogs.csv'
        sample_dogs = pd.read_csv('../../data/raw/version0_5/Adoptable_dogs_20221202_withExtras.csv', low_memory=False,header=0,index_col=0)
        sample_dogs = sample_dogs.dropna(subset=['primary_photo_cropped.full'])
        preferences = pd.DataFrame(columns=['user_name', 'dog_id', 'preference'])
        if not os.path.isfile(saveFile):
            self.appendDFToCSV_void(preferences,saveFile) # make file from scratch if it doesn't already exist
        if 'sample_dogs' not in st.session_state:
            st.session_state.sample_dogs=sample_dogs
        if 'saveFile' not in st.session_state:
            st.session_state.saveFile=saveFile
        if 'preferences' not in st.session_state:
            st.session_state.preferences=preferences

        # initialize session state for key dog instance variables if they don't already exist
        current_dog = sample_dogs.sample()
        display_name = current_dog['name'].values[0]
        display_description = str(current_dog['description_x'].values)
        display_image= self.find_photo(current_dog).values
        env_children = str(current_dog['environment.children'].values)
        env_dogs = str(current_dog['environment.dogs'].values)
        env_cats  = str(current_dog['environment.cats'].values)
        house_trained = str(current_dog['attributes.house_trained'].values)
        special_needs = str(current_dog['attributes.special_needs'].values)
        breed_group = str(current_dog['group'].values)
        groom_freq = str(current_dog['grooming_frequency_category'].values)
        shed_freq = str(current_dog['shedding_category'].values)
        energy_type = str(current_dog['energy_level_category'].values)
        train_type = str(current_dog['trainability_category'].values)
        demeanor = str(current_dog['demeanor_category'].values)
        breed = str(current_dog['breeds.primary'].values)

        if 'display_name' not in st.session_state:
            st.session_state.display_name=display_name
        if 'display_description' not in st.session_state:
            st.session_state.display_description=display_description
        if 'display_image' not in st.session_state:
            st.session_state.display_image=display_image
        if 'current_dog' not in st.session_state:
            st.session_state.current_dog=current_dog
        if 'env_children' not in st.session_state:
            st.session_state.env_children=env_children
        if 'env_dogs' not in st.session_state:
            st.session_state.env_dogs=env_dogs
        if 'env_cats' not in st.session_state:
            st.session_state.env_cats=env_cats
        if 'house_trained' not in st.session_state:
            st.session_state.house_trained=house_trained
        if 'special_needs' not in st.session_state:
            st.session_state.special_needs=special_needs
        if 'breed_group' not in st.session_state:
            st.session_state.breed_group=breed_group
        if 'groom_freq' not in st.session_state:
            st.session_state.groom_freq=groom_freq
        if 'shed_freq' not in st.session_state:
            st.session_state.shed_freq=shed_freq
        if 'energy_type' not in st.session_state:
            st.session_state.energy_type=energy_type
        if 'train_type' not in st.session_state:
            st.session_state.train_type=train_type
        if 'demeanor' not in st.session_state:
            st.session_state.demeanor=demeanor
        if 'breed' not in st.session_state:
            st.session_state.breed=breed
        # set up actual first dog for user
        self.new_dog()


# ==============================================================================

dogs_petmatch = DogsPetmatch()

dogs_petmatch.initial_setup()

# access saved values from session
display_name=st.session_state.display_name
display_description=st.session_state.display_description
display_image=st.session_state.display_image
current_dog=st.session_state.current_dog
env_children = st.session_state.env_children
env_dogs = st.session_state.env_dogs
env_cats  = st.session_state.env_cats
house_trained = st.session_state.house_trained
special_needs = st.session_state.special_needs
breed_group = st.session_state.breed_group
groom_freq = st.session_state.groom_freq
shed_freq = st.session_state.shed_freq
energy_type = st.session_state.energy_type
train_type = st.session_state.train_type
demeanor = st.session_state.demeanor
breed = st.session_state.breed

st.write(display_image[0])

# st.image('https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/58980756/6/?bust=1669602382&width=600')
st.title('PetMatch Playground')

if display_image is not None:
    st.image(display_image[0])

# photo
st.header(display_name)
st.write(display_description)
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

col1, col2 = st.columns([1,1])
with col1:
    if st.button('dislike'):
        dogs_petmatch.disliked(current_dog) 
        st.experimental_rerun() # required so UI reflects current values
with col2:
    if st.button('like'):
        dogs_petmatch.liked(current_dog) 
        st.experimental_rerun() # required so UI reflects current values