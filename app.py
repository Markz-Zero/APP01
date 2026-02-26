import streamlit as st
from PIL import Image

st.title("THIS IS A SIMULATION")

st.header("this is a lesser simulation")
st.write("this one is not a simulation.")

image = Image.open("winds.png")
st.image(image, caption="background")

texto = st.text_input('Escribe algo', 'Este no es tu texto')
st.write('El texto escrito es', texto)
