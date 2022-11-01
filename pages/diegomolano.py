import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote - Diego Molano Aponte", page_icon="🗳️")

st.title('Novus Vote 🗳️ - Diego Molano')
st.header("Centrales de Mando para la Operación Política y Electoral")
st.write("Focaliza el monitoreo de todos tus frentes")

etapa = st.select_slider(
    'Selecciona la etapa de campaña a monitorizar:',
    options=['Diagnóstico', 'Pre Campaña', 'Campaña', 'Día E', 'Post Campaña'])

if etapa = 'Diagnóstico':
    st.write('Los monitores que necesitas para ', etapa, 'son los siguientes:')
    st.header("Radiografía de Posicionamiento")
    st.header("Radiografía de Reputación")
    st.header("Radiografía de Votación Histórica")

    







st.write("""
**Credits**
- Software build by `Novus Wilber` with `Registraduría General de la Nación` data
""")
st.write('---')


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
