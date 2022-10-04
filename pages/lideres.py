import streamlit as st

st.title('Novus Vote 🗳️')
st.header("Sistema de Gestión de Líderes Electorales 🎯")

st.write("Formulario de Registro👋")



picture = st.camera_input("1. Identifique su rostro")

if picture:
    st.image(picture)
    st.write('Analizaremos el sentimiento de estas imagenes y te informaremos')

    
a = st.text_input('1. Número de Cédula')

b = st.text_input('2. Municipio de influencia ')

c = st.text_input('3. ¿Cuántos votos máximo puede gestionar?')

if a and b and c:
  st.write('Estamos preparando un Mando con el análisis de la potencia que genera <<',a, '>>, a partir de su web <<', b, '>> y en especial para el producto <<', c, '>>')
