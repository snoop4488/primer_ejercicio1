import streamlit as st 
from PIL import Image
st.title("mi primer app")



st.header("en este espacio desarrollo mi app")
image= Image.open("nacional.png")

st.image(image,caption ='nacional')

texto= st.text_input('solo nacional a morir',texto)
