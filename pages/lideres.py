import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
    st.write('Analizaremos el sentimiento de estas imagenes y te informaremos')
