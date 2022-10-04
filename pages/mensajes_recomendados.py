import streamlit as st
import pandas as pd
import numpy as np

st.title('Novus Vote 🗳️')
st.header("Sistema de Recomendación de Mensajes Territoriales 🎯")

st.write("Configura los parámetros para unos mensajes más potentes ⚙️")


st.radio('Selecciona el tono de los mensajes:', ['Buen humor', 'Beligerante', 'Conciliador', 'Educación', 'Salud', 'Movilidad'], key="fuente")

