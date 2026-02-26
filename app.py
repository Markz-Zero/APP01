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
    resp1 = st.checkbox('true')
    resp2 = st.checkbox('false')
    if resp1:
       st.write('correct')
    if resp2:
        st.write("you are fooling yourself")
    if resp1 and resp2:
        st.write("you are wise")
  
with col2:
    st.subheader("this one is also correct")
    modo = st.radio("What's the best food", ('pizza', 'coffee', 'avocado'))
    if modo == 'pizza':
       st.write('really?')
    if modo == 'coffee':
       st.write('that is a drink')
    if modo == 'avocado':
       st.write('you are weird')
