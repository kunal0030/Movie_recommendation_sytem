import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movie = []
    for i in movies_list:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load((open('similarity.pkl','rb')))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Enter the movie',
    movies['title'].values.tolist(),  # convert to list
    index=0  # pick first movie as default
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation :
        st.write(i)