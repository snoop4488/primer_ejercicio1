import streamlit as st 
st.title("mi primer app")

from PIL import image

st.header("en este espacio desarrollo mi app")
image= Image.open("nacional.png")

st.image(image,caption ='nacional')
