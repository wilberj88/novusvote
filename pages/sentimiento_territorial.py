

import streamlit as st

st.title('Hola, soy Atento 🤖')
a = st.text_input('¿Cuál es el perfil que quieres analizar?')

if a:
  st.write('Hola, ya estoy investigando sobre ',a, 'pronto te enviaré mi análisis de sentimiento 🤖 por cada red social donde aparezca')
