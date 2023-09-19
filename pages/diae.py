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


colored_header(
    label="Mando Día E - 29/Oct/2023",
    description="Desagrega por tipos de votantes",
    color_name="violet-70",
)



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
st.markdown('CONCLUSIONES MONITOR 4: POTENCIALES VOTANTES 🗳️')
st.text('La radiografía del TOP3 de perfiles de votantes más afines al CANDIDATO es: adultos mayores de 50 años, emprendedores mayores de 30 años y jóvenes estudiantes entre 20 y 25 años')
st.text('Concentrar la comunicación en el TOP3 de perfiles en los barrios X, Y y Z puede llevar las probabilidades de victoria por encima del 85%')

#ALARMA 1: CUMPLIMIENTOS DE METAS PARA FIRMAS Y VOTOS
#ALARMA 2: CUMPLIMIENTOS DE METAS PARA INFLUENCIA
#ALARMA 3: CUMPLIMIENTOS DE METAS PARA SENTIMIENTO FAVORABLE

#RECOMENDACIONES 1: PARA MÁS VOTOS
#RECOMENDACIONES 2: PARA MÁS INFLUENCIA
#RECOMENDACIONES 3: PARA MÁS SENTIMIENTO FAVORABLE






#ALARMAS
st.header("Alarmas de Bajo Cumplimiento de Metas ⚠️")
alarma1, alarma2, alarma3 = st.columns(3)
alarma1.metric("Electores por Alcanzar", "1/2/18", "-85%prom")
alarma2.metric("Electores por Influir", "16h.13h.18h", "-73%prom")
alarma3.metric("Electores por Convencer", "8-32-33", "485%prom")
chart_data = pd.DataFrame(np.random.randn(23, 3), columns=["Alcanzados", "Influenciados", "Convencidos"])
st.area_chart(chart_data)    
st.write('ID TOP 1 Perfil de menor Influencia', 1)
st.write('ID TOP 2 Perfil de menor Convencimiento', 2)
st.write('ID TOP 3 Perfil de menor Interacción', 18)
st.markdown('CONCLUSIONES ALARMAS ⚠️:')
st.text('Falta enfocar el alcance en los barrios X, Y y Z en los perfiles A, B y C')
st.text('Las horas de menor influencia son las 7pm-5am')



#RECOMENDACIONES
st.header("Recomendaciones para Aumentar Votos, Influencia y Sentimiento Favorable 🧠")
rec1, rec2, rec3 = st.columns(3)
rec1.metric("Horario de Mayor Influencia", "4pm", "85%prom")
rec2.metric("Horario de Mayor Convencimiento", "ID_08", "73%prom")
rec3.metric("Zonas de Mayor Impacto", "1-2-18", "-45%prom")
st.text('Potenciales zonas de mayor Influencia y Convencimiento')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])
st.map(df)
st.markdown('CONCLUSIONES RECOMENDACIONES 🧠:')
st.text('Se puede crecer 117% la votación si se intensifican los mensajes en los horarios de 8am - 1pm')
st.text('Se puede aumentar la influencia general en 35% si se enfocan en los barrios ID_007 y ID_004')
st.caption('Todos los análisis son representativos únicamente entre el día/mes/años y el día/mes/año con sus días ☀️ y con sus noches 🌛')
