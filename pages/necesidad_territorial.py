import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Análisis de Necesidades Territoriales")

st.radio('Selecciona la tipología de necesidad:', ['Acceso a Servicios Públicos Básicos', 'Empleo', 'Internet', 'Educación', 'Salud', 'Movilidad'], key="fuente")
