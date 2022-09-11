import streamlit as st
from PIL import Image

image1 = Image.open("images/memory-game.png")
image2 = Image.open("images/chicago-eats.png")
image3 = Image.open("images/quickflix.png")
image4 = Image.open("images/album-collector.png")
image5 = Image.open("images/daily.png")



st.title("Projects")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Memory Game", "Chicago Eats", "QuickFlix", "Album Collector", "Daily"])

with tab1:
    st.header("Memory Card Game")
    st.write("The memory card game was built using HTML, CSS and JavaScript.")
    st.write("[Launch the game here!](https://marianag11.github.io/GA-Project-1--Game-/)")
    st.image(image1, width=450)

with tab2:
    st.header("Chicago Eats")
    st.write("Chicago Eats is a restaurant guide for places to eat. This project was built using JavaScript, CSS, EJS, Node.js, Express, MongoDB and Google Oauth.")
    st.write("[View the app here!](https://project-2-ga.herokuapp.com)")
    st.image(image2, width=450)

with tab3:
    st.header("QuickFlix")
    st.write("QuickFlix is an app that brings the best movies of Netflix, Hulu, and Amazon Prime to one place! It is a group project built using Python, Django and Django Authentication.")
    st.write("[Launch the app!](https://quickflixmovies.herokuapp.com)")
    st.image(image3, width=450)
    
with tab4:
    st.header("Album Collector")
    st.write("Album Collector is an application that allows users to collect their favorite albums. This project was built using Python, Django and AWS.")
    st.write("[start your collection!](https://albumcollection.herokuapp.com/albums/)")
    st.image(image4, width=450)
    
with tab5:
    st.header("Daily")
    st.write("Daily is an app where users can track their workouts and upload photos they took that day. This project was built using React, JS, Express.js and JSX.")
    st.write("[Launch the app!](https://dailyworkouts.herokuapp.com/login)")
    st.image(image5, width=450)