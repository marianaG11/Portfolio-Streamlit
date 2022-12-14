import streamlit as st

st.title("About Me")
st.write("I am currently a Software Engineer Intern at Adobe. Prior to becoming an intern, I attended General Assembly Bootcamp through the Adobe Digital Academy. I graduated college with a Bachelor's of Science in Psychology. I have 6 years of experience in customer service which has allowed me to gain excellent communication skills, attention to detail and problem solving skills. I am passionate about contributing high quality solutions to projects and teams.")

st.subheader("[View more on GitHub](https://github.com/marianaG11)")

st.write("---")
st.subheader("Skills")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Technical:")
        st.write(
                """
                - JavaScript
                - Python3
                - Django
                - React
                - Express.js
                - Mongoose
                - Node.js
                - MongoDB
                - PostgreSQL
                - HTML5
                - CSS3
                - VS Code
                - Git and GitHub
                """)
        st.write("Proficient in English and Spanish")
