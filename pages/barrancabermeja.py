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



st.write('Votaciones Gobernanción 2019 en Bca')


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



st.title('PRE CAMPAÑA - Históricos 2015, 2019 y Proyecciones 2023')

st.header("Históricos")
st.write("2015 Resultados E-14 por Zonas")



st.write("2019 Resultados E-14 por Zonas")
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Ganador_Castro", "2do_Orozco", "3ro_Morales"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 8", "Zona 9"],
    },
    "series": [
        {
            "name": "Ganador_Castro",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [9549, 11314, 10390, 12513, 12728, 4977, 2935, 84, 8905],
        },
        {
            "name": "2do_Orozco",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [10013, 9513, 9712, 11971, 12824, 5638, 2562, 80, 7957],
        },
        {
            "name": "3ro_Morales",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [2055, 4196, 4228, 4887, 3776, 678, 1143, 39, 528],
        },
    ],
}
st_echarts(options=options, height="500px")




st.title("Combinación Top3 Votos Válidos en 2015 y 2019")
def render_basic_radar():
    option = {
        "title": {"text": "Zonas Alcaldía Valledupar 🗳️"},
        "legend": {"data": ["Ganador 2015", "2do 2015", "3ro 2015", "Ganador 2019", "2do 2019", "3ro 2019"]},
        "radar": {
            "indicator": [
                {"name": "Zona 1", "max": 14000},
                {"name": "Zona 2", "max": 14000},
                {"name": "Zona 3", "max": 14000},
                {"name": "Zona 4", "max": 14000},
                {"name": "Zona 5", "max": 14000},
                {"name": "Zona 6", "max": 14000},
                {"name": "Zona 7", "max": 14000},
                {"name": "Zona 8", "max": 14000},
                {"name": "Zona 9", "max": 14000},
            ]
        },
        "series": [
            {
                "name": "Votos por Zonas",
                "type": "radar",
                "data": [
                    {
                        "value": [10898, 12260, 10461, 13667, 11792, 4659, 4364, 152, 5931],
                        "name": "Ganador 2015",
                    },
                    {
                        "value": [7055, 6004, 5288, 6842, 7077, 4127, 2267, 58, 3337],
                        "name": "2do 2015",
                    },
                    {
                        "value": [2273, 2792, 2419, 2954, 2437, 974, 916, 16, 2863],
                        "name": "3ro 2015",
                    },
                    {
                        "value": [9549, 11314, 10390, 12513, 12728, 4977, 2935, 84, 8095],
                        "name": "Ganador 2019",
                    },
                    {
                        "value": [10013, 9513, 9712, 11971, 12824, 5638, 2562, 80, 7957],
                        "name": "2do 2019",
                    },
                    {
                        "value": [2055, 4196, 4228, 4887, 3776, 678, 1143, 39, 528],
                        "name": "3ro 2019",
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

st.header("Proyecciones 2023")

st.write("Votos válidos proyectados por zonas para 2023")
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
            "name": "Proyección Votos Válidos por Zonas 2023",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 28789, "name": "Zona 1"},
                {"value": 33532, "name": "Zona 2"},
                {"value": 31805, "name": "Zona 3"},
                {"value": 39217, "name": "Zona 4"},
                {"value": 39268, "name": "Zona 5"},
                {"value": 14663, "name": "Zona 6"},
                {"value": 8707, "name": "Zona 7"},
                {"value": 307, "name": "Zona 8"},
                {"value": 20531, "name": "Zona 9"},
            ],
        }
    ],
}
st_echarts(
    options=option, height="600px",
)

st.write('---')
st.header("Votos requeridos para ganar Alcaldía 2023 dado rango histórico")
zonas = ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 8", "Zona 9"]
n_zonas = len(zonas)

women_salary = [11228, 13078, 12404, 15294, 15314, 5719, 3396, 120, 8007]
men_salary = [13819, 16095, 15267, 18824, 18848, 7038, 4179, 147, 9855]

df = pd.DataFrame(dict(zonas=zonas*2, salary=men_salary + women_salary,
                       escenario=["Alto"]*n_zonas + ["Bajo"]*n_zonas))

# Use column names of df for the different parameters x, y, color, ...
fig = px.scatter(df, x="salary", y="zonas", color="escenario",
                 title="Entre el 39,7% y el 48,5%",
                 labels={"salary":"Votos válidos mínimos para ser Alcalde Valledupar en 2023"} # customize axis label
                )
st.plotly_chart(fig, theme="streamlit")

st.write('---')
st.title("Desagregación de votos en 2019 por mesa de votación, barrios y zonas")
#datos
df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [10.473583, -73.248639],
columns=['lat', 'lon'])
st.pydeck_chart(pdk.Deck(
map_style=None,
initial_view_state=pdk.ViewState(
latitude=10.473583,
longitude=-73.248639,
zoom=11,
pitch=50,
),
layers=[
pdk.Layer(
   'HexagonLayer',
   data=df,
   get_position='[lon, lat]',
   radius=200,
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

st.write('---')

st.title("Predicción de votos válidos en Alcaldía Valledupar 2023 por puesto de votación y zonas")
#datos
df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [10.473583, -73.248639],
columns=['lat', 'lon'])
st.pydeck_chart(pdk.Deck(
map_style=None,
initial_view_state=pdk.ViewState(
latitude=10.473583,
longitude=-73.248639,
zoom=11,
pitch=50,
),
layers=[
pdk.Layer(
   'HexagonLayer',
   data=df,
   get_position='[lon, lat]',
   radius=200,
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
st.write('---')

st.header('Conclusiones PRE CAMPAÑA - Tareas Campaña')
meta = 84558
st.write('Votos mínimos para aspirar a posesionarse Alcalde de Valledupar:', meta) 
st.write('Ritmo de votos mínimos por hora para aspirar a posesionarse Alcalde de Valledupar:', meta/8) 
st.write('Ritmo de votos mínimos por minuto para aspirar a posesionarse Alcalde de Valledupar:', meta/480) 
st.write('Importancia de Zonas por Votos: Zona 5 > Zona 4 > Zona 2 > Zona 3 > Zona 1 > Zona 9 > Zona 6 > Zona 7 > Zona 8')



#META
