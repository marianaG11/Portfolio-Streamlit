import streamlit as st

st.title("Projects")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Memory Game", "Chicago Eats", "QuickFlix", "Album Collector", "Daily"])

with tab1:
    st.header("Memory Card Game")
    st.write("The memory card game was built using HTML, CSS and JavaScript.")
    st.write("Launch the game here! ")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("Chicago Eats")
    st.write("Chicago Eats is a restaurant guide for places to eat. This project was built using JavaScript, CSS, EJS, Node.js, Express, MongoDB and Google Oauth.")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("QuickFlix")
    st.write("QuickFlix is an app that brings the best movies of Netflix, Hulu, and Amazon Prime to one place! It is a group project built using Python, Django and Django Authentication.")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
with tab4:
    st.header("Album Collector")
    st.write("Album Collector is an application that allows users to collect their favorite albums. This project was built using Python, Django and AWS.")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
with tab5:
    st.header("Daily")
    st.write("Daily is an app where users can track their workouts and upload photos they took that day. This project was built using React, JS, Express.js and JSX.")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)