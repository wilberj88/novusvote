import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Mandos para Campañas Electorales Exitosas")

st.write("""
**Cuatro (4) Centrales para las etapas de tu campaña:**
- 🗳️: `PRE CAMPAÑA: metas y requisitos`
- 🧑‍⚖️: `CAMPAÑA: necesidades y soluciones`
- 💲: `DÍA ELECTORAL: cronograma y monitoreo`
- 🧭: `POST CAMPAÑA: resultados, mensajes por territorios y próximos pasos`
""")

if st.button('Calcular diagnóstico gratuito'):
    meta = st.slider('¿Cuántos votos estimas necesitar para posecionarte?', 0, 100000)
