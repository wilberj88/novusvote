import streamlit as st

st.title('Novus Vote 🗳️')
st.header("Sistema de Gestión de Líderes Electorales 🎯")

st.write("Formulario de Registro👋")



picture = st.camera_input("1. Identifique su rostro")

if picture:
    st.image(picture)
    st.write('Analizaremos el sentimiento de estas imagenes y te informaremos')

    
    a = st.text_input('¿Cuál es el nombre de la competencia?')

b = st.text_input('¿Cuál es su pagina web?')

c = st.text_input('¿Cuál es el producto o servicio de tu mayor interés?')

if a and b and c:
  st.write('Estamos preparando un Mando con el análisis de la competencia que genera <<',a, '>>, a partir de su web <<', b, '>> y en especial para el producto <<', c, '>>')
