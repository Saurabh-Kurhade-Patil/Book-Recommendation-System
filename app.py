import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np

def recommend_movie(movie):
    movie_index = mov[mov['title'] == movie].index[0]
    distances = simi[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommend_movie_names=[]
    for i in movie_list[1:6]:
        movie_id = mov.iloc[[i[0]]].movie_id
        recommend_movie_names.append(mov.iloc[i[0]].title)

    return recommend_movie_names

st.header('Movie Recommendation system')
simi = pd.read_pickle('pkl/similarity.pkl')
mov = pd.read_pickle('pkl/movies.pkl')

movie_list = mov['title'].values
selected_movie = st.selectbox('select movie',movie_list)

if st.button('show recommendation'):
    recommend_movie_names = recommend_movie(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movie_names[0])
    with col2:
        st.text(recommend_movie_names[1])
    with col3:
        st.text(recommend_movie_names[2])
    with col4:
        st.text(recommend_movie_names[3])
    with col5:
        st.text(recommend_movie_names[4])

