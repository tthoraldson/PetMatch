import streamlit as st
import pandas as pd
import os

def new_cat():
    current_cat = sample_cats.sample()
    display_name = current_cat['name'].values[0]
    display_description = current_cat['description']
    find_photo(current_cat)

def disliked(current_cat):
    pd.concat([preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 0})], ignore_index=True)
    new_cat()
    print('disliked')
    appendDFToCSV_void(preferences,file) #save dataframe to csv in append mode

def liked(current_cat):
    pd.concat([preferences, pd.DataFrame({'user_name': user, 'cat_id': current_cat['id'], 'preference': 1})], ignore_index=True)
    print('liked')
    appendDFToCSV_void(preferences,file) #save dataframe to csv in append mode

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
            df.to_csv(csvFilePath, mode='+a', index=False, sep=sep,header=headers)
    except PermissionError:
        pass

# ==============================================================================
file = '../../data/rankings/petmatch_rankings.csv'
sample_cats = pd.read_csv('../../data/raw/version0_5/Adoptable_cats_20221125.csv', low_memory=False,header=0,index_col=0)
sample_cats = sample_cats.dropna(subset=['primary_photo_cropped.full'])
preferences = pd.DataFrame(columns=['user_name', 'cat_id', 'preference'])
appendDFToCSV_void(preferences,file) # make file from scratch if it doesn't already exist
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
