import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️", page_icon="🗳️")

#TITULO
st.title('Novus Vote 🗳️ - Módulo de Votaciones')

#SUBTITULO
st.write('---')
st.write("""
**Análisis de Ritmos Mínimos Requeridos para Ganar:**
- 🎯: `Votos Totales`
- 👥: `líderes territoriales`
- 🗺️: `Territorios`
- 🚌: `Transporte`
- 🍕: `Alimentación`
""")
st.write("""
**Sistema de Alarmas para:**
- ⏰ : `Retrasos en Cumplimientos Operativos de líderes territoriales`
""")
st.write("""
**Sistema de Recomendación para:**
- 📈:  `Más Votos, Influencia y Sentimientos favorables`
""")
st.write('---')
st.markdown('Versión Ejemplo Borrador - Cotiza tu versión personalizada en www.novusvote.com')


#CONFIGURACIÓN DEL MANDO
territorio = st.selectbox("Indica el Territorio",
        ("Bogotá", "Medellín", "Cali", "Bucaramanga", "Barrancabermeja"),
    )
categoria = st.radio(
        "Indica la categoría de campaña👇 ",
        options=['Gobernación', 'Asamblea Departamental','Alcaldía', 'Concejo', 'Junta de Acción Comunal'],
    )
st.slider('¿Cuál es la meta de votos?', 0, 300000, key="meta")


#meta = st.number_input('Ingresa la META DE VOTACIÓN del candidat@', min_value=1000, max_value=100000, value=10000)


if territorio and categoria and meta:
        st.write('El ritmo de votos por minuto es de: ', meta/4800)
        st.write('El ritmo de votos por hora es de: ', meta/8)
        
         
