import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Mandos para Campañas Electorales Exitosas")

st.markdown(
  """
  Cada etapa de la capaña tiene sus ritmos, sus metas y sus Mandos:
  - 📆 _    PRE CAMPAÑA: Meta electoral, Requerimientos Territoriales y Competencia Histórica
  - 🧠 _    CAMPAÑA: Líderes, Necesidades, Tendencias, Contrincantes y Propuestas por Territorios
  - 📢 _    DÍA ELECTORAL: Líderes, Testigos, Jurados, Defensores y Logística
  - 🏢 _    POST CAMPAÑA: Votos Logrados-Disputados-Perdidos, Defensores, Reposición proyectada, De Propuestas a Hechos
  
  EMPIEZA TU CAMPAÑA ELECTORAL AHORA 🕰 APROVECHA NUESTRO DIAGNÓSTICO GRATUITO
  """
)


meta = st.slider('¿Cuántos votos estimas necesitar para posecionarte?', 0, 100000)
