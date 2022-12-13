import streamlit as st
import pandas as pd

# settings
pd.options.display.max_colwidth = 8000

sample_cats = pd.read_csv('data/raw/version0_5/Adoptable_cats_20221125.csv')
st.write(sample_cats.head())
preferences = pd.DataFrame(columns=['user_name', 'cat_id', 'preference'])
current_cat = sample_cats.sample()
display_name = current_cat['name'].values[0]
#display_image = current_cat['image'][0]
display_description = current_cat['description'].values[0]


def new_cat():
    current_cat = sample_cats.sample()

def disliked(current_cat):
    preferences.append({'user_name': user, 'cat_id': current_cat['id'], 'preference': 'dislike'})
    new_cat()
    print('disliked')

def liked(current_cat):
    preferences.append({'user_name': user, 'cat_id': current_cat['id'], 'preference': 'dislike'})
    st.balloons()
    print('liked')
# ==============================================================================

# st.image('https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/58980756/6/?bust=1669602382&width=600')
st.title('PetMatch Playground')

user = st.selectbox(label='Select a user', options=['Theresa', 'Denise', 'Matt'])

# photo
st.header(display_name)
print(display_description)
st.text(display_description)


col1, col2 = st.columns([1,1])
with col1:
    if st.button('dislike'):
        disliked(current_cat)
with col2:
    if st.button('like'):
        liked(current_cat)
