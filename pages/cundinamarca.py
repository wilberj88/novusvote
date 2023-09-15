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
add_logo("https://images.app.goo.gl/Apr7qizCdGAj1eoe9")
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
