import pickle
import pandas as pd
import streamlit as st

movies = pickle.load(open('movie_dict.pkl', mode='rb'))
data = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl', mode='rb'))


def recommend(movie):
    movie_index = data[data['title'] == movie].index[0]

    distance = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(data.iloc[i[0]].title)

    return recommendations


st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    data['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)