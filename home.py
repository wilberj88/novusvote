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

st.write("Son 4 etapas y 4 ritmos distintos: Pre Campaña + Campaña + Día Elección + Post Campaña ")

items = [
    {"id": 1, "content": "2023-06-15", "start": "2023-07-29"},
    {"id": 2, "content": "2023-10-21", "start": "2023-07-30"},
    {"id": 3, "content": "2023-11-06", "start": "2023-10-22"},
    {"id": 4, "content": "2023-11-07", "start": "2024-01-30"},
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




st.title("Test Plan")

items = [
    {"id": 1, "content": "Early shift", "start": "2022-10-17T08:00:00", "end": "2022-10-17T16:00:00", "group": "1"},

    {"id": 2, "content": "Early shift", "start": "2022-10-17T11:00:00", "end": "2022-10-17T15:00:00", "group": "2"},

    {"id": 3, "content": "Early shift", "start": "2022-10-17T10:00:00", "end": "2022-10-17T18:00:00", "group": "3"}
]

groups = [
    {"id": 1, "content": "Worker 1", "style": "color: black; background-color: #a9a9a98F;"},
    {"id": 2, "content": "Worker 2", "style": "color: black; background-color: #a9a9a98F;"},
    {"id": 3, "content": "Worker 3", "style": "color: black; background-color: #a9a9a98F;"}
]

timeline = st_timeline(items, groups=groups, options={"selectable": True, 
                                                      "multiselect": True, 
                                                      "zoomable": True, 
                                                      "verticalScroll": True, 
                                                      "stack": False,
                                                      "height": 200, 
                                                      "margin": {"axis": 5}, 
                                                      "groupHeightMode": "auto", 
                                                      "orientation": {"axis": "top", "item": "top"}})

st.subheader("Selected item")
st.write(timeline)
