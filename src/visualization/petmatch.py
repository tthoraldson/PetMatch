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

    user = st.selectbox(label='Select a user', options=['Theresa', 'Denise', 'Matt'])

    return 'intro was run'

intro()
    

class CatsPetmatch:

    # TODO do not hardcode path to load cats data
    cats_path = '/app/data/version0_5/Adoptable_cats_20221125.csv'

    # instance attrs
    def __init__(self):
        self.preferences = pd.DataFrame(columns=['user_name', 'cat_id', 'preference'])
        self.animal_type = 'cats'
        self.sample_cats = None
        self.display_name = None
        self.display_image = None
        self.display_description = None

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
        current_cat = self.sample_cats.sample()
        self.display_name = current_cat['name'].values[0]
        self.display_description = current_cat['description']
        self.find_photo(current_cat)

    # registers a disliked cat
    def disliked(self,current_cat):
        pd.concat([self.preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 0})], ignore_index=True)
        self.new_cat()
        print('disliked')

    # registers a liked cat
    def liked(self,current_cat):
        pd.concat([self.preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 1})], ignore_index=True)
        print('liked')

    # find cat photo(s)
    def find_photo(self,current_cat):
        print(vars(current_cat['photos']))
        if not current_cat['photos'].empty:

            return current_cat['primary_photo_cropped.full']



# ==============================================================================


cats_petmatch = CatsPetmatch()

# display_name = current_cat['name'].values[0]

# display_image = find_photo(current_cat).values

# display_description = str(current_cat['description'])
# st.write(current_cat['primary_photo_cropped.full'])

# if display_image is not None:
#     st.image(display_image[0])

# st.title('PetMatch Playground')




col1, col2 = st.columns([1,1])
with col1:
    if st.button('dislike'):
        cats_petmatch.disliked(
                cats_petmatch.current_cat
            )
with col2:
    if st.button('like'):
        cats_petmatch.liked(
                cats_petmatch.current_cat
            )

# # photo
st.header(cats_petmatch.display_name)
st.write(cats_petmatch.display_description)