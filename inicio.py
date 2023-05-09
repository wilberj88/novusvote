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

st.header("Centrales de Mando para Campañas Electorales Exitosas")

st.write("Pre Campaña + Campaña + Día Elección + Post Campaña ")

_, col2, _ = st.beta_columns([1, 2, 1])

with col2:
    st.title("Pre Campaña")
