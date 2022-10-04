import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Análisis de Sentimiento Territorial")

st.write("Selecciona el territorio a analizar:")

df = pd.DataFrame(
    np.random.randn([7.4, -73.8],
    columns=['lat', 'lon'])

st.map(df)

