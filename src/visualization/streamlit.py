import streamlit as st
import pandas as pd

def new_cat():
    current_cat = sample_cats.sample()
    display_name = current_cat['name'].values[0]
    display_description = current_cat['description']
    find_photo(current_cat)

def disliked(current_cat):
    pd.concat([preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 0})], ignore_index=True)
    new_cat()
    print('disliked')

def liked(current_cat):
    pd.concat([preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 1})], ignore_index=True)
    print('liked')

def find_photo(current_cat):
    print(vars(current_cat['photos']))
    if not current_cat['photos'].empty:

        return current_cat['primary_photo_cropped.full']



# ==============================================================================
cats_path = '/app/data/version0_5/Adoptable_cats_20221125.csv'
sample_cats = pd.read_csv(cats_path, low_memory=False)
sample_cats = sample_cats.dropna(subset=['primary_photo_cropped.full'])

preferences = pd.DataFrame(columns=['user_name', 'cat_id', 'preference'])
current_cat = sample_cats.sample()
display_name = current_cat['name'].values[0]

display_image = find_photo(current_cat).values

display_description = str(current_cat['description'])
st.write(current_cat['primary_photo_cropped.full'])

# st.image('https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/58980756/6/?bust=1669602382&width=600')

if display_image is not None:
    st.image(display_image[0])

st.title('PetMatch Playground')

user = st.selectbox(label='Select a user', options=['Theresa', 'Denise', 'Matt'])

# photo
st.header(display_name)
st.write(display_description)


col1, col2 = st.columns([1,1])
with col1:
    if st.button('dislike'):
        disliked(current_cat)
with col2:
    if st.button('like'):
        liked(current_cat)
