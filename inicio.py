import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
from streamlit_timeline import st_timeline

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Tecnología Electoral", page_icon="🗳️")

st.title('Novus Vote 🗳️')

st.header("Tecnología para Campañas Electorales Exitosas")
wt.write("_Si no te hacemos ganar, te diremos exactamente por qué perdiste_")

st.write("Pre Campaña + Campaña + Día Elección + Post Campaña ")

items = [
    {"id": 1, "content": "2022-10-20", "start": "2022-10-20"},
    {"id": 2, "content": "2022-10-09", "start": "2022-10-09"},
    {"id": 3, "content": "2022-10-18", "start": "2022-10-18"},
    {"id": 4, "content": "2022-10-16", "start": "2022-10-16"},
    {"id": 5, "content": "2022-10-25", "start": "2022-10-25"},
    {"id": 6, "content": "2022-10-27", "start": "2022-10-27"},
]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)
