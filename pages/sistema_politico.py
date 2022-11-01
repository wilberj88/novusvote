import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Sistema Inteligente de Gestión Política")



st.radio('Selecciona el monitor a configurar para tu PRE campaña:', ['Firmas','Votos Históricos', 'Votantes Previos', 'Votos Potenciales', 'Potenciales Votantes'])

st.radio('Selecciona el monitor a configurar para tu campaña:', ['Líderes', 'Testigos', 'Voluntarios', 'Jurados'])

st.radio('Selecciona el monitor a configurar para tu POST campaña:', ['Defensores'])
