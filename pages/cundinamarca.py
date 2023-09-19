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
import folium
from streamlit_folium import st_folium
import time
from streamlit_card import card
from PIL import Image
from streamlit_extras.app_logo import add_logo


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Cundinamarca", page_icon="🗳️")

# TITULO
add_logo("http://placekitten.com/120/120")
image = Image.open('pages/logonovusvote.jpg')
st.image(image, caption='Novus Tech World')
st.title('Novus Vote 🗳️ - Gobernación Cundinamarca 2023')

st.title('Central de PRE CAMPAÑA')
st.subheader(':red[Votación Histórica 2015-2019], :blue[Proyecciones 2023] y :green[Requisitos para Ganar] 🏆')
st.header("1. Históricos: Datos procesados 🛠️")

st.subheader("Votación Gobernación 2015")
option1 = {
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
            "name": "Candidaturas",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 545201, "name": "Jorge Emilio Rey 545K Coalición CR.U.Asi.Maiz"},
                {"value": 360813, "name": "Nacy Patricia Gutierrez 360K Partido Col Justa Libres"},
                {"value": 25956, "name": "Rafel Antonio Ballen Molina 26K Polo"},
                {"value": 91100, "name": "Voto en blanco 91K"},
            ],
        }
    ],
}
st_echarts(options=option1, height="600px")



st.subheader("Votación Gobernación 2019")
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
            "name": "Candidaturas",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 58987, "name": "Ricardo Mestizo Reyes 59K - Coalicioón Alternativa"},
                {"value": 48465, "name": "Pedro Enrique Caycedo 48K - Partido Col Justa Libres"},
                {"value": 634470, "name": "Nicolás García Bustos 634K - Coalición Gran Cundinamarca"},
                {"value": 52702, "name": "Germán Mauricio Escobar Latorre 52K - Partido Colombia Renaciente"},
                {"value": 99348, "name": "Wilson Antonio Florez Vanegas 99K - Coalición Cund Lider"},
                {"value": 244269, "name": "Voto en blanco 244K"},
            ],
        }
    ],
}
st_echarts(options=option, height="600px")



st.write('---')

st.header("2. Proyecciones a 29 octubre de 2023")
proyecciones = ["Habilitados", "Votantes", "Votación Válida", "Abstención", "Votos en Blanco"]

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


st.header("3. Requisitos para ganar")
validos2023 = 900000
meta2023 = validos2023*0.36
st.write('El ritmo de votos requeridos por la campaña por hora es de: ', meta2023/8)  
st.write('El ritmo de votos requeridos por la campaña por minuto es de: ', meta2023/480)

meta_zona_1 = 10290
meta_zona_2 = 11986
meta_zona_3 = 11368
meta_zona_4 = 14018
meta_zona_5 = 14036
meta_zona_6 = 5241
meta_zona_7 = 3112
meta_zona_8 = 110
meta_zona_9 = 7338


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


st.write('Ritmo de votación por generos requerido')
st.header("Votos requeridos por género para ganar Alcaldía Valledupar 2023 en escenario histórico")
st.subheader("Suponiendo crecimiento electoral del 18% y participación de victoria del 39%")
st.write("Mujeres: 43.378 ; Hombres: 41.180")
option = {
    "legend": {},
    "tooltip": {"trigger": "axis", "showContent": False},
    "dataset": {
        "source": [
            ["product", "Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 8", "Zona 9"],
            ["Mujer", 5760, 6709, 6363, 7846, 7856, 2934, 1742, 61, 4108],
            ["Hombre", 5468, 6369, 6041, 7448, 7458, 2785, 1654, 58, 3899],
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
            "type": "pie",
            "id": "pie",
            "radius": "30%",
            "center": ["50%", "25%"],
            "emphasis": {"focus": "data"},
            "label": {"formatter": "{b}: {@2012} ({d}%)"},
            "encode": {"itemName": "product", "value": "Zona 9", "tooltip": "Zona 9"},
        },
    ],
}
st_echarts(option, height="500px", key="echarts")

st.write('Ritmo de votación por edades requerido')
meta_18_25 = meta2023*0.16
meta_25_30 = meta2023*0.14
meta_30_35 = meta2023*0.13
meta_35_40 = meta2023*0.12
meta_40_45 = meta2023*0.11
meta_45_50 = meta2023*0.10
meta_50_55 = meta2023*0.09
meta_55_60 = meta2023*0.08
meta_mas_60 = meta2023*0.07
options = {
            "title": {"text": "Votos x Zonas"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
            },
            "legend": {"data": ["18-25años", "25-30años", "30-35años", "35-40años", "40-45años", "45-50años", "50-55años", "55-60", "+60años"]},
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
                    "name": "18-25años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_18_25*0.1, meta_18_25*0.2, meta_18_25*0.35, meta_18_25*0.45, meta_18_25*0.5, meta_18_25*0.75, meta_18_25],
                },
                {
                    "name": "25-30años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_25_30*0.1, meta_25_30*0.2, meta_25_30*0.35, meta_25_30*0.45, meta_25_30*0.5, meta_25_30*0.75, meta_25_30],
                },
                {
                    "name": "30-35años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_30_35*0.1, meta_30_35*0.2, meta_30_35*0.35, meta_30_35*0.45, meta_30_35*0.5, meta_30_35*0.75, meta_30_35],
                },
                  {
                    "name": "35-40años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_35_40*0.1, meta_35_40*0.2, meta_35_40*0.35, meta_35_40*0.45, meta_35_40*0.5, meta_35_40*0.75, meta_35_40],
                },
                 {
                    "name": "40-45años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_40_45*0.1, meta_40_45*0.2, meta_40_45*0.35, meta_40_45*0.45, meta_40_45*0.5, meta_40_45*0.75, meta_40_45],
                },
                  {
                    "name": "45-50años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_45_50*0.1, meta_45_50*0.2, meta_45_50*0.35, meta_45_50*0.45, meta_45_50*0.5, meta_45_50*0.75, meta_45_50],
                },
                  {
                    "name": "50-55años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_50_55*0.1, meta_50_55*0.2, meta_50_55*0.35, meta_50_55*0.45, meta_50_55*0.5, meta_50_55*0.75, meta_50_55],
                },
                  {
                    "name": "55-60años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_55_60*0.1, meta_55_60*0.2, meta_55_60*0.35, meta_55_60*0.45, meta_55_60*0.5, meta_55_60*0.75, meta_55_60],
                },
                  {
                    "name": "+60años",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_mas_60*0.1, meta_mas_60*0.2, meta_mas_60*0.35, meta_mas_60*0.45, meta_mas_60*0.5, meta_mas_60*0.75, meta_mas_60],
                },
            ],
        }
st_echarts(options=options, height="400px") 





st.write('---')
st.title('Central de CAMPAÑA')
col1, col2, col3, col4 = st.columns(4)
col1.metric("Correos", "300000", "14%")
col2.metric("Celulares", "4500000", "-18%")
col3.metric("ID_Meta", "1000000", "13%")
col4.metric("ID_Google", "950000", "18%")

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


current_time = time.ctime()
st.write("A día de hoy a las: ", current_time)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Derecha", "5.1M", "14%")
col2.metric("Izquierda", "4.7M", "-18%")
col3.metric("Centro", "3.9M", "13%")
col4.metric("Ambientales", "2.6M", "18%")
