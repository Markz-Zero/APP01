import streamlit as st

st.title("THIS IS A SIMULATION")

st.header("this is a lesser simulation")
st.write("this one is not a simulation.")

image = Image.open("winds.png")
st.image(image, caption="background")
