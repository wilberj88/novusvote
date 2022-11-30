import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Sistemas Inteligentes para Conseguir Votos")

st.write("Bienvenidos al futuro electoral 👋")


st.markdown(
  """
  En esta web encontrarás los módulos que necesita tu campaña:
  - 📆 _    Sistema Político: control electoral mediante monitor de votaciones, líderes, testigos, voluntarios, jurados y competencia
  - 🧠 _    Sistema Programático: coyuntura local en necesidades y sentimientos, propuestas y discurso
  - 📢 _     Sistema Comunicaciones: monitor de noticias, creación y difusión de contenido
  - 🏢 _    Sistema Administrativo: Tesorería, Logística, Jurídica y Auditoría
  
  EMPIEZA TU CAMPAÑA ELECTORAL AHORA 🕰 CON NUESTRO DIAGNÓSTICO GRATUITO
  """
)


acelerometro1 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 30, "name": "Firmas"}],
            }
        ],
    }

st_echarts(options=acelerometro1)


acelerometro2 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 50, "name": "Votos"}],
            }
        ],
    }

st_echarts(options=acelerometro2)


acelerometro3 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 80, "name": "Sentimiento"}],
            }
        ],
    }

st_echarts(options=acelerometro3)
