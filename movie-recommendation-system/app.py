import streamlit as st
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))



def recommend(movie):
    #get movie index
    movie_index = movies[movies['title'] == movie].index[0]
    # get the cosine with all
    distances = similarity[movie_index]
    # get top sililar
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x : x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)

    return recommend_movies

st.title('Movie Recommendation')


selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_list
)
if st.button('Press to Recommend'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)



