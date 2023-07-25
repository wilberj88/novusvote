import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64
import graphviz
from pyecharts import options as opts
from pyecharts.charts import Graph
import time

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️", page_icon="🗳️")

#TITULO
st.title('Novus Vote 🗳️ - Modelación Intención de Voto V.0.1')
st.header("Desde la Escucha Social hasta la Votación Válida proyectada")


st.header("Escucha Social")
st.write("Desagregada por Redes Sociales")
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Sentimiento Positivo", "Sentimiento Negativo", "Sentimiento Neutro"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Red Social 1", "Red Social 2", "Red Social 3", "Red Social 4", "Red Social 5", "Red Social 6", "Red Social 7", "Red Social 8", "Red Social 9"],
    },
    "series": [
        {
            "name": "Sentimiento Positivo",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [10898, 12260, 10461, 13667, 11792, 4659, 4364, 152, 5931],
        },
        {
            "name": "Sentimiento Negativo",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [7055, 6004, 5288, 6842, 7077, 4127, 2267, 58, 3337],
        },
        {
            "name": "Sentimiento Neutro",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [2273, 2792, 2419, 2954, 2437, 974, 916, 16, 2863],
        },
    ],
}
st_echarts(options=options, height="500px")


st.header("Ponderaciones Poblacionales")
st.write("Participación de edades por zonas")
option = {
    "legend": {"top": "bottom"},
    "toolbox": {
        "show": True,
        "feature": {
            "mark": {"show": True},
            "dataView": {"show": True, "readOnly": False},
            "restore": {"show": True},
            "saveAsImage": {"show": True},
        },
    },
    "series": [
        {
            "name": "Participación de grupos de edades",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 28789, "name": "18 a 25 años"},
                {"value": 33532, "name": "26 a 30 años"},
                {"value": 31805, "name": "31 a 35 años"},
                {"value": 39217, "name": "36 a 40 años"},
                {"value": 39268, "name": "41 a 45 años"},
                {"value": 14663, "name": "46 a 50 años"},
                {"value": 8707, "name": "51 a 55 años"},
                {"value": 307, "name": "56 a 60 años"},
                {"value": 20531, "name": "Más de 65 años"},
            ],
        }
    ],
}
st_echarts(
    options=option, height="600px",
)

st.write('---')
st.title("Votación histórica por partidos o ideologías")
option = {
    "legend": {},
    "tooltip": {"trigger": "axis", "showContent": False},
    "dataset": {
        "source": [
            ["product", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
            ["Conservador", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
            ["Verde", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
            ["Polo", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
            ["Liberal", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
        ]
    },
    "xAxis": {"type": "category"},
    "yAxis": {"gridIndex": 0},
    "grid": {"top": "55%"},
    "series": [
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "pie",
            "id": "pie",
            "radius": "30%",
            "center": ["50%", "25%"],
            "emphasis": {"focus": "data"},
            "label": {"formatter": "{b}: {@2012} ({d}%)"},
            "encode": {"itemName": "product", "value": "Junio", "tooltip": "Junio"},
        },
    ],
}
st_echarts(option, height="500px", key="echarts")
st.write('---')
st.header("Intención de Votos a Presidencia")
current_time = time.ctime()
st.write("A día de hoy a las: ", current_time)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Derecha", "5.1M", "14%")
col2.metric("Izquierda", "4.7M", "-18%")
col3.metric("Centro", "3.9M", "13%")
col4.metric("Ambientales", "2.6M", "18%")
