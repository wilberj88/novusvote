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

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ CAMPAÑA", page_icon="🗳️")

#TITULO
st.title('Novus Vote 🗳️ - Mando Campaña')
st.header('1. Puestos de Votación 🗺️')

#columnas_to_keep = ["Nombre", "Votos Válidos 2019", "Latitud", "Longitud"]
data = pd.read_csv('pages/datos/Votos Válidos procesados Valledupar 2015-2019 - Puro Puestos.csv')
data_pura = data.dropna()
st.dataframe(data_pura)

st.subheader('Identificación por: Zona, Puesto de Zona, Puesto Total, Nombre, Meta y Caudal')

zona_1 = pd.DataFrame({
   'lon':[10.473583, 10.474139, 10.478472, 10.468500, 10.469667, 10.474139],
   'lat':[-73.248639, -73.25125, -73.245361, -73.247278, -73.238056, -73.25125],
   'name':['PV1 COL. Nacional Loperena', 'PV2 ESC Bellas Artes', 'PV3 UDES', 'PV4 COL Prudencia Daza', 'PV5 COL SantoDomingo', 'PV6 COL Parroquial El Carmelo'],
   'value':[7588, 4933,3771, 2735, 5666, 57]
}, dtype=str)


st.write('Georreferenciación por Puestos de Votación Zona 1, 2, 3, 4, 5, 6, 7 y 8. Pendiente zona 9')
# center on Liberty Bell, add marker
m = folium.Map(location=[10.4735, -73.2486], zoom_start=13)
#zona1
folium.Marker(
    [10.47358, -73.248639], popup="Z1 PV1 PV1 COL Nacional Loperena 3de10K", tooltip="Z1 PV1 PV1 COL Nacional Loperena. 3K de 8K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.474139, -73.25125], popup="Z1 PV2 PV2 ESC Bellas Artes. 2K de 5K", tooltip="Z2 PV2 PV2 ESC Bellas Artes. 2K de 5K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.478472, -73.245361], popup="Z1 PV3 PV3 UDES. 1,5K de 4K", tooltip="Z1 PV3 PV3 UDES. 1,5K de 4K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.468500, -73.247278], popup="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", tooltip="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.469667, -73.238056], popup="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", tooltip="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", icon=folium.Icon(icon='cloud')
).add_to(m)
folium.Marker(
    [10.474130, -73.251115], popup="PV6 COL Parroquial El Carmelo (Nuevo 2023)", tooltip="PV6 COL Parroquial El Carmelo", icon=folium.Icon(icon='cloud')
).add_to(m)
#zona2
folium.Marker(
    [10.46006, -73.22889], popup="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", tooltip="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.46322, -73.23575], popup="Z2 PV2 PV8 I.E. Manuel Germán Cuello. 2K de 4K", tooltip="Z2 PV1 PV8 I.E. Manuel Germán Cuello. 2K de 4K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.45389, -73.24211], popup="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", tooltip="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", icon=folium.Icon(icon='flag')
).add_to(m)
folium.Marker(
    [10.45100, -73.23672], popup="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", tooltip="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", icon=folium.Icon(icon='flag')
).add_to(m)
#zona3
folium.Marker(
    [10.44578, -73.25128], popup="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", tooltip="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", icon=folium.Icon(icon='star')
).add_to(m)
folium.Marker(
    [10.44950, -73.25075], popup="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", tooltip="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", icon=folium.Icon(icon='star')
).add_to(m)
folium.Marker(
    [10.45131, -73.25711], popup="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", tooltip="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", icon=folium.Icon(icon='star')
).add_to(m)
folium.Marker(
    [10.45714, -73.25153], popup="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", tooltip="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", icon=folium.Icon(icon='star')
).add_to(m)
folium.Marker(
    [10.43650, -73.25356], popup="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", tooltip="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", icon=folium.Icon(icon='star')
).add_to(m)
#zona4
folium.Marker(
    [10.45358, -73.26678], popup="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", tooltip="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    [10.45892, -73.25958], popup="Z4 PV2 PV21 COL Nacionalizado UPAR. 3,5K de 8K", tooltip="Z4 PV2 PV21 COL Nacionalizado UPAR 8K. 3,5K de 8K", icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    [10.46157, -73.26789], popup="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", tooltip="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    [10.46661, -73.25814], popup="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", tooltip="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    [10.44381, -73.27533], popup="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", tooltip="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", icon=folium.Icon(icon='info-sign')
).add_to(m)
#zona5
folium.Marker(
    [10.47242, -73.26011], popup="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", tooltip="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47242, -73.26011], popup="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", tooltip="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47928, -73.27719], popup="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", tooltip="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.47842, -73.29089], popup="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", tooltip="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", icon=folium.Icon(icon='bicycle')
).add_to(m)
folium.Marker(
    [10.48606, -73.28081], popup="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", tooltip="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", icon=folium.Icon(icon='bicycle')
).add_to(m)
#zona6
folium.Marker(
    [10.48044, -73.24781], popup="Z6 PV1 PV33 COL. Pablo Sexto 5K", tooltip="Z6 PV1 PV33 COL. Pablo Sexto 5K", color='red'
).add_to(m)
folium.Marker(
    [10.48181, -73.25644], popup="Z6 PV2 PV34 CONC.San Joaquin 4K", tooltip="Z6 PV2 PV34 CONC.San Joaquin 4K", color='red'
).add_to(m)
folium.Marker(
    [10.49319, -73.26533], popup="Z6 PV3 PV35 COL. Sagrada Familia 3K", tooltip="Z6 PV3 PV35 COL. Sagrada Familia 3K", color='red'
).add_to(m)
#zona7
folium.Marker(
    [10.47475, -73.25969], popup="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", tooltip="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", color='red'
).add_to(m)
#zona8
folium.Marker(
    [10.46442, -73.25625], popup="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", tooltip="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", color='red'
).add_to(m)
folium.Marker(
    [10.44664, -73.30750], popup="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", tooltip="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", color='red'
).add_to(m)
st_data = st_folium(m, width=725)


st.header('2. Equipos por Puestos de Votación 🗳️')
st.subheader('Territoriales + Género + Edad')

st.title("Palabras clave por Barrio")
data = [
    {"name": name, "value": value}
    for name, value in [
        ("Energia", "999"),
        ("Salud", "888"),
        ("Educación", "777"),
        ("Vivienda", "688"),
        ("Alimentación", "588"),
        ("Negocios", "516"),
        ("Carreteras", "515"),
        ("Puentes", "483"),
        ("Hospitales", "462"),
        ("Ciclovías", "449"),
        ("Talento", "429"),
        ("Tecnología", "407"),
        ("Innovación", "406"),
        ("Seguridad", "906"),
        ("Crimen", "386"),
        ("Servicios", "985"),
        ("Microtráfico", "375"),
        ("Deportes", "355"),
        ("Futbol", "355"),
        ("Baloncesto", "335"),
        ("Microfutbol", "324"),
    ]
]
wordcloud_option = {"series": [{"type": "wordCloud", "data": data}]}
st_echarts(wordcloud_option)
st.write('---')
st.header('3. Tareas para Ganar 🏆')
st.subheader('Tanquear el Funnel de Conversión Votante por Puesto de Votación')

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
st.subheader('Cumplimiento de tareas por equipos con corte a: ', current_time)


col1, col2, col3 = st.columns(3)
with col1:
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
                "data": [{"value": 10, "name": "Territoriales"}],
            }
        ],
    }

  st_echarts(options=acelerometro1)

with col2:
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
                "data": [{"value": 15, "name": "Género"}],
            }
        ],
    }

  st_echarts(options=acelerometro2)

with col3:
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
                "data": [{"value": 20, "name": "Edades"}],
            }
        ],
    }
  st_echarts(options=acelerometro3)

st.write("""
🧠 Algoritmo adaptador de propuestas en mensajes personalizados por barrios y perfiles psicológicos
- 🥺: `Deseos`
- 🥵: `Miedos`
- 😭: `Sufrimientos`
- 🙏: `Esperanzas`
- 💰: `Necesidades`
""")
st.video("https://youtu.be/7831NGClsrM")
st.header("Asistentes Virtuales para gestionar equipos de campaña 🤖")
# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('Bienvenida', 'Introducción')
graph.edge('Introducción', 'Identificación')
graph.edge('Identificación', 'Bienvenida')
graph.edge('Bienvenida', 'Entrenamiento')
graph.edge('Entrenamiento', 'Teoría')
graph.edge('Entrenamiento', 'Pruebas')
graph.edge('Entrenamiento', 'Reporte y Ranking TOTAL')
graph.edge('Pruebas', 'Examen')
graph.edge('Examen', 'DíaE')
graph.edge('DíaE', 'ReporteDíaE')
graph.edge('DíaE', 'Reporte y Ranking TOTAL')
graph.edge('ReporteDíaE', 'Reporte y Ranking TOTAL')
st.graphviz_chart(graph)
st.write("""
Todo el proceso de atención, desde la bienvenida hasta el ranking de resultados por equipos
- 🗣️: `Voluntarios`
- 🦶: `Líderes`
- 🧑‍⚖️: `Jurados`
- 🕵️: `Testigos`
- 💰: `Ciudadanía`
- ⚖️: `Defensores`
- 🚧: `Logística`
""")
st.write('---')

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



#SUBTITULO
st.write('---')
st.write("""
**Nueve (9) Centrales de Mando para:**
- 🗺: `Necesidades Territoriales`
- 💛: `Sentimientos Digitales`
- 🧭: `Propuestas`
- 🚧: `Proyectos`
- 🗣️: `Voluntarios`
- 🦶: `Líderes`
- 🧑‍⚖️: `Jurados`
- 🕵️: `Testigos`
- 💰: `Financiación`
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
