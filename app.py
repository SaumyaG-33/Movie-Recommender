import pickle
import pandas as pd
import requests
import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #000066, #9966ff);
    }
    .stImage {
        border-radius: 10px;
    }
    .stSubheader {
        white-space: nowrap;
    }
    .css-1lcbmhc {
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def fetch_post(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=93cea9ba5af618c0e40c9cea50ae2780&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

st.sidebar.title('About')
st.sidebar.info('This app suggests movies based on your chosen title, using data from the IMDb 5000 movies dataset. It matches films by comparing the cast, genre, director, and plot to find the best recommendation for you. Get started by picking one movie from the dropdown menu on the left. There are 5000 movies to choose from!')

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
          # fetch poster from the API
        recommended_movies_posters.append(fetch_post(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender!')


selected_movie_names = st.selectbox(
    'Pick one of your favorite movies, and I will recommend a similar one!', (movies['title'].values) 
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_names)

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
    
    
