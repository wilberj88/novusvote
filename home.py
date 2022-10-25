import streamlit as st
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
  - 📆 _    Sistema Político: control electoral mediante monitor de votaciones, líderes, testigos, avanzadas y competencia
  - 🧠 _    Sistema Programático: coyuntura local en necesidades y sentimientos, propuestas y discurso
  - 📢 _     Sistema Comunicaciones: monitor de noticias, creación y difusión de contenido
  - 🏢 _    Sistema Administrativo: Tesorería, Logística, Jurídica y Auditoría
  
  EMPIEZA TU CAMPAÑA ELECTORAL AHORA 🕰
  """
)
