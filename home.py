import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts
from streamlit_timeline import st_timeline
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64
from pyecharts import options as opts
from pyecharts.charts import Graph


st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Tecnología Electoral", page_icon="🗳️")

st.title('Novus Vote 🗳️')

st.header("Tecnología para Campañas Electorales Exitosas")
st.write("_Si no te hacemos ganar, te diremos exactamente dónde y por qué perdiste_")

st.write("Pre Campaña + Campaña + Día Elección + Post Campaña ")

items = [
    {"id": 1, "PRECampaña desde": "2023-06-15", "start": "2023-07-29"},
#    {"id": 2, "Campaña": "2022-10-09", "start": "2022-10-09"},
#    {"id": 3, "DíaE": "2022-10-18", "start": "2022-10-18"},
#    {"id": 4, "POSTCampaña": "2022-10-16", "start": "2022-10-16"},
]

#items = [
#    {"id": 1, "PRE Campaña inicia:": "2023-06-15", "PRE Campaña finaliza:": "2023-07-29"},
#    {"id": 2, "Campaña inicia:": "2023-07-29", "Campaña finaliza": "2023-10-21"},
#    {"id": 3, "Día E inicia:": "2023-10-22", "Día E finalizada:": "2023-11-06"},
#    {"id": 4, "POST Campaña inicia": "2022-10-16", "POST Campaña finaliza": "2022-10-16"},
#]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)
