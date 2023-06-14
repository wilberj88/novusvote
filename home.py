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
    {"id": "PRE Campaña", "Inicia": "2023-06-15", "Finaliza": "2022-07-29"},
    {"id": "Campaña", "Campaña": "2022-10-09", "start": "2022-10-09"},
    {"id": "DíaE", "Día E": "2022-10-18", "start": "2022-10-18"},
    {"id": "POST Campaña", "Post Campaña": "2022-10-16", "start": "2022-10-16"},
    ]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)
