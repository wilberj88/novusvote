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


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Valledupar PRE CAMPAÑA", page_icon="🗳️")

#TITULO
st.title('Novus Vote 🗳️ - Alcaldía Valledupar V.0.6')


st.header('PRE CAMPAÑA - Históricos Votos Válidos')

st.header("Resultados E-14 en 2015 por Zonas")
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Ganador_Ramirez", "2do_Gonzalez", "3ro_Fernandez"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 8", "Zona 9"],
    },
    "series": [
        {
            "name": "Ganador_Ramirez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [10898, 12260, 10461, 13667, 11792, 4659, 4364, 152, 5931],
        },
        {
            "name": "2do_Gonzalez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [7055, 6004, 5288, 6842, 7077, 4127, 2267, 58, 3337],
        },
        {
            "name": "3ro_Fernandez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [2273, 2792, 2419, 2954, 2437, 974, 916, 16, 2863],
        },
    ],
}
st_echarts(options=options, height="500px")
          
st.write('---')
st.title("Top3 Votos Válidos en 2015 y 2019")
def render_basic_radar():
    option = {
        "title": {"text": "Zonas Alcaldía Valledupar 🗳️"},
        "legend": {"data": ["Ganador 2015", "2do 2015", "3ro 2015", "Ganador 2019", "2do 2019", "3ro 2019"]},
        "radar": {
            "indicator": [
                {"name": "Zona 1", "max": 14000},
                {"name": "Zona 2", "max": 14000},
                {"name": "Zona 3", "max": 14000},
                {"name": "Zona 4", "max": 14000},
                {"name": "Zona 5", "max": 14000},
                {"name": "Zona 6", "max": 14000},
                {"name": "Zona 7", "max": 14000},
                {"name": "Zona 8", "max": 14000},
                {"name": "Zona 9", "max": 14000},
            ]
        },
        "series": [
            {
                "name": "Votos por Zonas",
                "type": "radar",
                "data": [
                    {
                        "value": [10898, 12260, 10461, 13667, 11792, 4659, 4364, 152, 5931],
                        "name": "Ganador 2015",
                    },
                    {
                        "value": [7055, 6004, 5288, 6842, 7077, 4127, 2267, 58, 3337],
                        "name": "2do 2015",
                    },
                    {
                        "value": [2273, 2792, 2419, 2954, 2437, 974, 916, 16, 2863],
                        "name": "3ro 2015",
                    },
                    {
                        "value": [9549, 11314, 10390, 12513, 12728, 4977, 2935, 84, 8095],
                        "name": "Ganador 2019",
                    },
                    {
                        "value": [10013, 9513, 9712, 11971, 12824, 5638, 2562, 80, 7957],
                        "name": "2do 2019",
                    },
                    {
                        "value": [2055, 4196, 4228, 4887, 3776, 678, 1143, 39, 528],
                        "name": "3ro 2019",
                    },
                ],
            }
        ],
    }
    st_echarts(option, height="500px")
ST_RADAR_DEMOS = {
    "Radar: Basic Radar": (
        render_basic_radar,
        "https://echarts.apache.org/examples/en/editor.html?c=radar",
    ),
}
render_basic_radar()

st.title("Top3 Partidos Políticos a Alcaldía en 2015 y 2019")
option = {
    "legend": {},
    "tooltip": {"trigger": "axis", "showContent": False},
    "dataset": {
        "source": [
            ["product", "1999", "2004", "2007", "2011", "2015", "2019"],
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
            "encode": {"itemName": "product", "value": "2019", "tooltip": "2019"},
        },
    ],
}
st_echarts(option, height="500px", key="echarts")
st.write('---')


st.header('CAMPAÑA - Requisitos')

#META
meta = 70000
st.write('Votos mínimos para aspirar a posesionarse Alcalde de Valledupar:', meta) 
