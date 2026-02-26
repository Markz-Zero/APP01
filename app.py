import streamlit as st
from PIL import Image

st.title("THIS IS A SIMULATION")

st.header("this is a lesser simulation")
st.write("this one is not a simulation.")

image = Image.open("winds.png")
st.image(image, caption="background")

texto = st.text_input('Escribe algo', 'Este no es tu texto')
st.write('El texto escrito es', texto)

st.subheader("Two paths")

col1, col2 = st.columns(2)

with col1:
    st.subheader("this is the first")
    st.write("choice is an illusion")
    resp = st.checkbox('true')
    if resp:
       st.write('correct')
  
with col2:
    st.subheader("this one is also correct")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('El tacto es fundamental para tu interfaz')
