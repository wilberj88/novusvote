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
from mitosheet.streamlit.v1 import spreadsheet

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Barrancabermeja 2023", page_icon="🗳️")

#TITULO
st.title('Novus Vote 🗳️ - Alcaldía Barrancabermeja')
st.header('Mando PRE Campaña - De Históricos a Proyecciones 29/10/2023')

st.write('Votaciones Alcaldía 2015')
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
                {"value": 31418, "name": "Dario Echeverry 31K"},
                {"value": 21909, "name": "Liliana De Cote 21K"},
                {"value": 21173, "name": "Horacio Henao 21K"},
                {"value": 20785, "name": "Jonathan Vasquez 20K"},
                {"value": 9145, "name": "Yaneth Mojica 9K"},
            ],
        }
    ],
}
st_echarts(
    options=option, height="600px",
)

st.write('---')
st.write('Votaciones Alcaldía 2019')
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Jonathan Vasquez", "Alfonso Eljach", "Claudia Andrade"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 98", "Zona 99"],
    },
    "series": [
        {
            "name": "Jonathan Vasquez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [4928, 3980, 5532, 3734, 5246, 3297, 3493, 11, 3519],
        },
        {
            "name": "Alfonso Eljach",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [9633, 7894, 8693, 6883, 8334, 4559, 4264, 70, 5489],
        },
        {
            "name": "Claudia Andrade",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [2005, 1624, 1973, 1605, 1865, 851, 932, 10, 1004],
        },
    ],
}
st_echarts(options=options, height="500px")
st.write('---')


st.write('Votaciones Gobernanción 2019 en Bca')
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Mauricio Aguilar", "Elkin Bueno", "Leonidas Gomez", "Angela Hernández"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 98", "Zona 99"],
    },
    "series": [
        {
            "name": "Mauricio Aguilar",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [4059, 3187, 4320, 2885, 4013, 2604, 2259, 20, 2694],
        },
        {
            "name": "Elkin Bueno",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [800, 654, 748, 434, 703, 405, 343, 9, 353],
        },
        {
            "name": "Leonidas Gomez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [7507, 6924, 6394, 5808, 6479, 2785, 3003, 26, 3091],
        },
        {
            "name": "Angela Hernández",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [3668, 2748, 3730, 2920, 3565, 2040, 2606, 15, 2902],
        },
    ],
}
st_echarts(options=options, height="500px")

st.write('---')
st.header('Máximas votaciones por zonas en BCA en 2019 tanto Alcaldía como Gobernación')
def render_basic_radar():
    option = {
        "title": {"text": "Frontera: 🗳️10K"},
        "legend": {"data": ["Alfonso Eljach", "Jonathan Vasquez", "Leonidas Gómez", "Mauricio Aguilar", "Elkin Bueno", "Ángela Hernández"]},
        "radar": {
            "indicator": [
                {"name": "Zona 1", "max": 10000},
                {"name": "Zona 2", "max": 10000},
                {"name": "Zona 3", "max": 10000},
                {"name": "Zona 4", "max": 10000},
                {"name": "Zona 5", "max": 10000},
                {"name": "Zona 6", "max": 10000},
                {"name": "Zona 7", "max": 10000},
                {"name": "Zona 8", "max": 10000},
                {"name": "Zona 9", "max": 10000},
            ]
        },
        "series": [
            {
                "name": "Votos por Zonas",
                "type": "radar",
                "data": [
                    {
                        "value": [9633, 7894, 8693, 6883, 8334, 4559, 4264, 70, 5489],
                        "name": "Alfonso Eljach",
                    },
                    {
                        "value": [4928, 3980, 5532, 3734, 5246, 3297, 3493, 11, 3519],
                        "name": "Jonathan Vasquez",
                    },
                    {
                        "value": [7507, 6924, 6394, 5808, 6479, 2785, 3003, 26, 3091],
                        "name": "Leonidas Gómez",
                    },
                    {
                        "value": [4059, 3187, 4320, 2885, 4013, 2604, 2259, 20, 2694],
                        "name": "Mauricio Aguilar",
                    },
                    {
                        "value": [800, 654, 748, 434, 703, 405, 343, 9, 353],
                        "name": "Elkin Bueno",
                    },
                    {
                        "value": [3668, 2748, 3730, 2920, 3565, 2040, 2606, 15, 2902],
                        "name": "Ángela Hernández",
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

st.write('---')


st.header('Mando Campaña  V.0.1')
st.write('Tareas por Territorios, Líderes, Equipos y Puestos de Votación')

st.header('Mando DíaE  V.0.1')
st.write('Monitor de Cumplimiento de Tareas por horas, minutos, territorios, líderes, equipos y Puestos de Votación')

st.header('Mando PostDíaE  V.0.1')
st.write('Monitor de Resultados con Ranking por niveles de cumplimiento')



df = pd.DataFrame({'Candidatos 2015': ["Echeverry", "DeCote", "HoracioHenao", "JonathanVasquez", "YanethMojica"], 'Votos Válidos 2015': [31418, 21909, 21173, 20785, 9145]})
st.write('Votaciones Alcaldía 2019')
df1 = pd.DataFrame({'Candidatos 2019': ["JonathanVasquez", "AlfonsoEljach", "ClaudiaPatricia"], 
                    'Zona1': [4928, 9633, 2005],
                    'Zona2': [3980, 7894, 1624],
                    'Zona3': [5532, 8693, 1973],
                    'Zona4': [3734, 6883, 1605],
                    'Zona5': [5246, 8334, 1865],
                    'Zona6': [3297, 4559, 851],
                    'Zona7': [3493, 4264, 932],
                    'Zona98': [11, 70, 10],
                    'Zona99': [3519, 5489, 1004],
                    'TotalCandidato': [33740, 55819, 11869],
                   })
new_dfs, _ = spreadsheet(df, df1, df_names=['df', 'df1'])
new_df = list(new_dfs.values())[0]
st.write(new_dfs)



st.write('---')

st.header('Conclusiones PRE CAMPAÑA - Tareas Campaña')
meta = 84558
#st.write('Votos mínimos para aspirar a posesionarse Alcalde de Barrancabermeja:', meta) 
#st.write('Ritmo de votos mínimos por hora para aspirar a posesionarse Alcalde de Valledupar:', meta/8) 
#st.write('Ritmo de votos mínimos por minuto para aspirar a posesionarse Alcalde de Valledupar:', meta/480) 
#st.write('Importancia de Zonas por Votos: Zona 5 > Zona 4 > Zona 2 > Zona 3 > Zona 1 > Zona 9 > Zona 6 > Zona 7 > Zona 8')



#META
