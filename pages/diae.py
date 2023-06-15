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
from streamlit_timeline import st_timeline

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️", page_icon="🗳️")

# SETTING BACKGROUND
#page_bg_img = f"""
#<style>
#[data-testid="stAppViewContainer"] > .main {{
#background-image: url("https://images.unsplash.com/photo-1602906530215-1bf5f4925279?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1527&q=80");
#background-size: 180%;
#background-position: top;
#background-repeat: no-repeat;
#background-attachment: local;
#}}
#[data-testid="stSidebar"] > div:first-child {{
#background-image: url("https://images.unsplash.com/photo-1603032813605-2c91e257e2ae?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8dm90b3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60");
#background-position: left; 
#background-repeat: no-repeat;
#background-attachment: local;
#}}
#[data-testid="stHeader"] {{
#background: rgba(0,0,0,0);
#}}
#[data-testid="stToolbar"] {{
#right: 2rem;
#}}
#</style>
#"""
#st.markdown(page_bg_img, unsafe_allow_html=True)



#TITULO
st.title('Novus Vote 🗳️ - Día E')
st.header("24 horas de monitoreo minuto a minuto")

st.title("Cronograma 📆 de trabajo por equipos 👥")

items = [
    {"id": 1, "content": "Early shift", "start": "2022-10-17T08:00:00", "end": "2022-10-17T16:00:00", "group": "1"},

    {"id": 2, "content": "Early shift", "start": "2022-10-17T11:00:00", "end": "2022-10-17T15:00:00", "group": "2"},

    {"id": 3, "content": "Early shift", "start": "2022-10-17T10:00:00", "end": "2022-10-17T18:00:00", "group": "3"}
]

groups = [
    {"id": 1, "content": "Worker 1", "style": "color: black; background-color: #a9a9a98F;"},
    {"id": 2, "content": "Worker 2", "style": "color: black; background-color: #a9a9a98F;"},
    {"id": 3, "content": "Worker 3", "style": "color: black; background-color: #a9a9a98F;"}
]

timeline = st_timeline(items, groups=groups, options={"selectable": True, 
                                                      "multiselect": True, 
                                                      "zoomable": True, 
                                                      "verticalScroll": True, 
                                                      "stack": False,
                                                      "height": 200, 
                                                      "margin": {"axis": 5}, 
                                                      "groupHeightMode": "auto", 
                                                      "orientation": {"axis": "top", "item": "top"}})

st.subheader("Selected item")
st.write(timeline)


#SUBTITULO
st.write('---')
st.write("""
**Cinco (5) Centrales de Mando para:**
- 🤔: `Paradoja por Perfiles de Votantes`
- 🫂: `Equipo: líderes, Jurados, Testigos y Defensores`
- 🚮: `Mesas Electorales`
- 🚌: `Transporte`
- 🦐: `Alimentación`
""")
st.write("""
**Sistema de Alarmas para:**
- ⏰ : `Retrasos en Cumplimientos de Metas`
""")
st.write("""
**Sistema de Recomendación para:**
- 📈:  `Más Votos, Influencia y Sentimientos favorables`
""")
st.write('---')
st.markdown('Versión Ejemplo Borrador - Cotiza tu versión personalizada en www.novusvote.com')

option = st.selectbox(
    'Elige la Circunscripción de tu Candidatura:',
    ('Gobernación', 'Asamblea', 'Alcaldía', 'Concejo', 'Comunas'))
if option:
    st.write('Datos históricos disponibles para ', option, 'desde el día/mes/año hasta el día/mes/año')

#MONITOR 1: NECESIDADES TERRITORIALES
st.header("Monitor 📺 de NECESIDADES TERRITORIALES 🗺 ")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Empleo", value = '250%', delta='17')
col2.metric("Educación", "195%", "13")
col3.metric("Salud", "87%", "7")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])
st.write("Desagregación geográfica de Empleo, Salud y Educación")
st.write(
    pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": 40.3875,
            "longitude": -3.7575416667,
            "zoom": 12,
            "pitch": 50},
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=150,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                ),
             pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                ),
        ],
        ))
st.markdown('CONCLUSIONES MONITOR 1: NECESIDADES TERRITORIALES 🗺')
st.text('Falta legalizar el 13% de las firmas requeridas para formalizar la candidatura')
st.text('Las zonas de mayor ubicación de firmas potenciales son Norte y Este en los barrios X, Y y Z')

#MONITOR 2: SENTIMIENTOS DIGITALES
#MONITOR 3: PROPUESTAS
#MONITOR 4: PROYECTOS
#MONITOR 5: VOLUNTARIOS
#MONITOR 6: LÍDERES
#MONITOR 7: JURADOS
#MONITOR 8: TESTIGOS
#MONITOR 9: FINANCIACIÓN
st.header("Monitor 📺 de Operación de FIRMAS ✍️")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Firmas Obtenidas", value = '250%', delta='17')
col2.metric("Firmas Tramitadas", "195%", "13")
col3.metric("Firmas Legalizadas", "87%", "7")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])
st.write("Desagregación geográfica de Firmas Potenciales, Obtenidas, Tramitadas y Legalizadas")
st.write(
    pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": 40.3875,
            "longitude": -3.7575416667,
            "zoom": 12,
            "pitch": 50},
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=150,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                ),
             pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                ),
        ],
        ))
st.markdown('CONCLUSIONES MONITOR 1: FIRMAS:')
st.text('Falta legalizar el 13% de las firmas requeridas para formalizar la candidatura')
st.text('Las zonas de mayor ubicación de firmas potenciales son Norte y Este en los barrios X, Y y Z')


#MONITOR 2: VOTOS
st.header("Monitor 📺 de Operación de VOTOS 🗳️")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Votos Gestionados", value = '150%', delta='17')
col2.metric("Votos en Gestión", "55%", "13")
col3.metric("Votos por Gestionar", "25%", "7")
st.text('Desagregación geográfica de la gestión de votos')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])
st.map(df)
st.markdown('CONCLUSIONES MONITOR 2: VOTOS 🗳️')
st.text('Falta gestionar el 45% de las votos requeridos para pelear la candidatura con probabilidad de victoria del 85%')
st.text('Las zonas de mayor ubicación de firmas potenciales son Norte y Este en los barrios X, Y y Z')



#MONITOR 3: CAUDAL ELECTORAL
st.header("Monitor 📺 de Operación de CAUDAL ELECTORAL 🌎")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Caudal Histórico", value = '15%', delta='11')
col2.metric("Caudal Última Elección", "55%", "13")
col3.metric("Caudal Próxima Elección", "25%", "7")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])
st.write("Desagregación geográfica del Caudal Electoral Histórico, Previo y Próximo con Abstenciones")
st.write(
    pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": 40.3875,
            "longitude": -3.7575416667,
            "zoom": 12,
            "pitch": 50},
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=150,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                ),
             pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                ),
        ],
        ))
st.markdown('CONCLUSIONES MONITOR 3: CAUDAL ELECTORAL 🗳️')
st.text('Falta abarcar el 45% del caudal electoral con mensajes personalizados para pelear la candidatura con probabilidad de victoria del 85%')
st.text('Las zonas de mayor ubicación de cuadal electoral son Norte y Este en los barrios X, Y y Z')


#MONITOR 4: POTENCIALES VOTANTES
st.header("Monitor 📺 de Operación de POTENCIALES VOTANTES 🎯")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Potenciales Votantes", value = '150%', delta='17')
col2.metric("Votantes Contactados", "55%", "13")
col3.metric("Votantes Influenciados", "25%", "7")
#data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
# Group data together
hist_data = [x1, x2, x3]
group_labels = ['Perfil TOP1 afinidad', 'Perfil TOP2 afinidad', 'Perfil TOP3 afinidad']
# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)
st.write('Top 3 de POTENCIALES VOTANTES MÁS AFINES')
st.write(pd.DataFrame({
    'Edades Perfiles Más Afines': [55, 32, 27],
    'Localidades Perfiles Más Afines': [1, 0, 2]}))
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])
st.write("Desagregación geográfica de Potenciales Votantes, Votantes Contactados, Votantes En Contacto y Votantes Influenciados")
st.write(
    pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": 40.3875,
            "longitude": -3.7575416667,
            "zoom": 12,
            "pitch": 50},
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=150,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                ),
             pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                ),
        ],
        ))
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
