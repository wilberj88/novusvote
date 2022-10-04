import streamlit as st

st.title('Novus Vote 🗳️')
st.header("Sistema de Gestión de Líderes Electorales 🎯")

st.write("Formulario de Registro👋")



picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
    st.write('Analizaremos el sentimiento de estas imagenes y te informaremos')
