import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Sistema Inteligente de Gestión Política")



st.radio('Selecciona el monitor a configurar:', ['Firmas','Votos Históricos', 'Votantes Previos', 'Votos Potenciales', 'Potenciales Votantes', 'Líderes', 'Testigos', 'Voluntarios', 'Jurados'])
