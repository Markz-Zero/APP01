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
    if resp1 and not resp2:
       st.write('correct')
    if resp2 and not resp1:
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

st.subheader("Buttons")
if st.button('Press it'):
    st.write('Why though?')
else:
    st.write('Maybe you should')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
