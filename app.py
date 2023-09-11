# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:55:06 2023

@author: Hritwij

"""

#%%
import streamlit as st
import pickle as pkl
import pandas as pd
import requests


movies = pd.read_pickle(open('movies.pkl','rb'))    # DataFrame
similarity = pkl.load(open('similarity.pkl','rb'))
ids_series = pd.read_pickle(open('moovie_id.pkl','rb'))

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0349f98abdafdc1d16363d54e6608285'
    response = requests.get(url)
    
    data = response.json()
    return 'https://image.tmdb.org/t/p/w185/' + data['poster_path']
    

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    rec_tupple = sorted(list(enumerate(similarity[movie_index])),
                        reverse = True, key = lambda x: x[1])[1:6]
    
    rec_list = []
    enumerated_id = []
    actual_id = []
    posters = []
    
    for i in rec_tupple:
        rec_list.append(movies['title'][i[0]])
        enumerated_id.append(i[0])
    
    for i in enumerated_id:
        actual_id.append(ids_series.loc[i])
        
    for i in actual_id:
        posters.append(fetch_poster(i))
        
    return rec_list, posters

    
        
st.title('Movie Recommendation System')
st.markdown('''by :orange[**Hritwij Kamble**] :sunglasses:''')

selected_movie_name = st.selectbox(
                                  'Select a Movie :',
                                  (movies['title'].values))

if st.button('Recommend',type='primary'):
    recommendations, posters = recommend(selected_movie_name)
    
   
    st.header(recommendations[0])
    st.image(posters[0])
    

    st.header(recommendations[1])
    st.image(posters[1])
    
   
    st.header(recommendations[2])
    st.image(posters[2])
    
    st.header(recommendations[3])
    st.image(posters[3])
    
    st.header(recommendations[4])
    st.image(posters[4])
        



