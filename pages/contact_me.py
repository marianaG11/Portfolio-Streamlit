import streamlit as st
from PIL import Image
image = Image.open("images/profile-pic.jpeg")
st.title("Contact Me")

col1, col2 = st.columns(2)

with col1:
    st.write("Email: mariana.garcia.16@icloud.com")
    st.write("[Connect with me on LinkedIn](https://www.linkedin.com/in/marianagarcia1/)")
    
    
with col2:
    st.image(image, width=350)