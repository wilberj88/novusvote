import streamlit as st
import st_echarts
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Sistemas Inteligentes para Conseguir Votos")

st.write("Bienvenidos al futuro electoral 👋")

options = {
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
                "data": [{"value": value, "name": "Score"}],
            }
        ],
    }

st_echarts(options=options, width="100%", key=0)


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
