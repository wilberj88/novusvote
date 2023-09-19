import streamlit as st
from streamlit_echarts import st_echarts
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64
from streamlit_timeline import st_timeline
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️", page_icon="🗳️")

#TITULO
st.title('Novus Vote 🗳️')

validos2023 = 900000
meta2023 = validos2023*0.36

meta_zona_1 = 10290
meta_zona_2 = 11986
meta_zona_3 = 11368
meta_zona_4 = 14018
meta_zona_5 = 14036
meta_zona_6 = 5241
meta_zona_7 = 3112
meta_zona_8 = 110
meta_zona_9 = 7338


colored_header(
    label="Mando Día E - 29/Oct/2023",
    description="Desagrega por tipos de votantes",
    color_name="violet-70",
)

colA, colB = st.columns(2)
with colA:
    st.write('El ritmo de votos requeridos por la campaña por hora es de: ', meta2023/8)  
with colB:
    st.write('El ritmo de votos requeridos por la campaña por minuto es de: ', meta2023/480)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Correos", "300000", "14%")
col2.metric("Celulares", "4500000", "-18%")
col3.metric("ID_Meta", "1000000", "13%")
col4.metric("ID_Google", "950000", "18%")

st.header('Votos requeridos por zonas para ganar Gobernación Cundinamarca 2023')
options = {
            "title": {"text": "Votos x Zonas"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
            },
            "legend": {"data": ["Zona_9", "Zona_8", "Zona_7", "Zona_6", "Zona_5", "Zona_4", "Zona_3", "Zona_2", "Zona_1"]},
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": ["10am", "11am", "12md", "1pm", "2pm", "3pm", "4pm"],
                }
            ],
            "yAxis": [{"type": "value"}],
            "series": [
                {
                    "name": "Zona_9",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_9*0.1, meta_zona_9*0.2, meta_zona_9*0.35, meta_zona_9*0.45, meta_zona_9*0.5, meta_zona_9*0.75, meta_zona_9],
                },
                {
                    "name": "Zona_8",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_8*0.1, meta_zona_8*0.2, meta_zona_8*0.35, meta_zona_8*0.45, meta_zona_8*0.5, meta_zona_8*0.75, meta_zona_8],
                },
                {
                    "name": "Zona_7",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_7*0.1, meta_zona_7*0.2, meta_zona_7*0.35, meta_zona_7*0.45, meta_zona_7*0.5, meta_zona_7*0.75, meta_zona_7],
                },
                  {
                    "name": "Zona_6",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_6*0.1, meta_zona_6*0.2, meta_zona_6*0.35, meta_zona_6*0.45, meta_zona_6*0.5, meta_zona_6*0.75, meta_zona_6],
                },
                 {
                    "name": "Zona_5",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                },
                  {
                    "name": "Zona_4",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                },
                  {
                    "name": "Zona_3",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                },
                  {
                    "name": "Zona_2",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                },
                  {
                    "name": "Zona_1",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                },
            ],
        }
st_echarts(options=options, height="400px") 


col6, col7 = st.columns(2)
with col6:
    option = {
        "title": {"text": "Eficacia de la Campaña", "subtext": "Porcentaje Conversión(%)"},
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c}%"},
        "toolbox": {
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {},
            }
        },
        "legend": {"data": ["Contactados", "Interesados", "Persuadidos", "Comprometidos", "Votantes"]},
        "series": [
            {
                "name": "Contactados",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "label": {"formatter": "{b}%"},
                "labelLine": {"show": False},
                "itemStyle": {"opacity": 0.7},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}预期: {c}%"}
                },
                "data": [
                    {"value": 60, "name": "Persuadidos"},
                    {"value": 40, "name": "Comprometidos"},
                    {"value": 20, "name": "Votantes"},
                    {"value": 80, "name": "Interesados"},
                    {"value": 100, "name": "Contactados"},
                ],
            },
            {
                "name": "Margen",
                "type": "funnel",
                "left": "10%",
                "width": "80%",
                "maxSize": "80%",
                "label": {"position": "inside", "formatter": "{c}%", "color": "#fff"},
                "itemStyle": {"opacity": 0.5, "borderColor": "#fff", "borderWidth": 2},
                "emphasis": {
                    "label": {"position": "inside", "formatter": "{b}实际: {c}%"}
                },
                "data": [
                    {"value": 30, "name": "Persuadidos"},
                    {"value": 10, "name": "Comprometidos"},
                    {"value": 5, "name": "Votantes"},
                    {"value": 50, "name": "Interesados"},
                    {"value": 80, "name": "Contactados"},
                ],
                "z": 100,
            },
        ],
    }
    st_echarts(option, height="500px")    

with col7:
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

col1, col2, col3 = st.columns(3)
with col1:
    card(
        title="Habilitados",
        text="2M",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )
with col2:
    card(
        title="Abstención",
        text="2M",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )
with col3:
    card(
        title="Votos Válidos",
        text="2M",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )
