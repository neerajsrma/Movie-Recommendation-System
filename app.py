import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c0dc896e477c3293d2277016b328f045'.format(movie_id))
    data = response.json()
    # return ('https://image.tmdb.org/t/p/w500' + data['poster_path'])
    # print(data)
    # st.text(data)
    if 'poster_path' in data:
        return f'https://image.tmdb.org/t/p/w500{data["poster_path"]}'
    else:
        return "No poster available"


def recommand(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommand_movie = []
    recommand_movie_poster = []
    for i in movie_list:
        movie_if = movie.iloc[i[0]].movie_id
        recommand_movie.append(movie.iloc[i[0]].title)
        recommand_movie_poster.append(fetch_poster(movie_if))
    return recommand_movie, recommand_movie_poster


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Film Fellow')

selected_movie_name = st.selectbox(
    'How would you like to connected?',
    movie['title'].values
)

if st.button('Recommand'):
    names, posters = recommand(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    