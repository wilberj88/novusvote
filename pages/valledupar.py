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


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Valledupar PRE CAMPAÑA", page_icon="🗳️")

#TITULO
st.title('Novus Vote 🗳️ - Alcaldía Valledupar 2023')

st.title('Central de PRE CAMPAÑA')
st.subheader('_Votación_ :red[Histórica 2015-2019], :blue[Proyecciones 2023] y :green[Requisitos para Ganar] 🏆')
st.header("1. Históricos: Datos procesados 🛠️")
#columnas_to_keep = ["Nombre", "Votos Válidos 2019", "Latitud", "Longitud"]
data = pd.read_csv('pages/datos/Votos Válidos procesados Valledupar 2015-2019 - Puro Puestos.csv')
data_pura = data.dropna()
st.dataframe(data_pura)

st.header("Votación Alcaldía 2015")

st.write("Resultados E-14 por Zonas")
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Ganador_Ramirez", "2do_Gonzalez", "3ro_Fernandez"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 8", "Zona 9"],
    },
    "series": [
        {
            "name": "Ganador_Ramirez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [10898, 12260, 10461, 13667, 11792, 4659, 4364, 152, 5931],
        },
        {
            "name": "2do_Gonzalez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [7055, 6004, 5288, 6842, 7077, 4127, 2267, 58, 3337],
        },
        {
            "name": "3ro_Fernandez",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [2273, 2792, 2419, 2954, 2437, 974, 916, 16, 2863],
        },
    ],
}
st_echarts(options=options, height="500px")

st.header("Votación Alcaldía 2019")
st.write("Resultados E-14 por Zonas")
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


st.header("Top 3 entre 2015 y 2019")
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

st.header('¿Qué dicen los datos históricos?')
st.write('1) Porcentaje mínimo para posesionarse Alcalde en Valledupar ha sido el 39%')
st.write('2) Porcentaje promedio de crecimiento de los votos válidos está en el 18%')
st.write('3) De las 7 zonas de la ciudad, las 5 primeras arrojan el 80% de la votación, siendo las zonas 4 y 5 las más grandes con 18,1% de participación cada una')


st.write('---')
st.title("2. Proyecciones a octubre 2023")
validos2023 = 215275
st.write('Número de votos válidos a la Alcaldía manteniendo crecimiento promedio en los votos: ', validos2023)
st.header('Votación por Zonas: el caudal a cautivar')
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
                {"value": 28789, "name": "Zona 1 28K (13,3%)"},
                {"value": 33532, "name": "Zona 2 33K (15,5%)"},
                {"value": 31805, "name": "Zona 3 31K (14,7%)"},
                {"value": 39217, "name": "Zona 4 39K (18,1%)"},
                {"value": 39268, "name": "Zona 5 39K (18,1%)"},
                {"value": 14663, "name": "Zona 6 14K (6,8%)"},
                {"value": 8707, "name": "Zona 7 8K (4%)"},
                {"value": 307, "name": "Zona 8 0,3K (0,1%)"},
                {"value": 20531, "name": "Zona 9 20K (9,5%)"},
            ],
        }
    ],
}
st_echarts(
    options=option, height="600px",
)
st.write('Número de votos válidos necesarios para ganar la Alcaldía con participación del 30% de los votos: ', validos2023*0.3)
st.write('Número de votos válidos necesarios para ganar la Alcaldía con participación del 33% de los votos: ', validos2023*0.33)
st.write('Número de votos válidos necesarios para ganar la Alcaldía con participación del 36% de los votos: ', validos2023*0.36)
st.write('Número de votos válidos necesarios para ganar la Alcaldía con participación del 39% de los votos: ', validos2023*0.39)
st.write('Proyección volumen de votación válida a la alcaldía por horas el domingo 29 de octubre:')
option = {
    "xAxis": {
        "type": "category",
        "data": ["9am", "10am", "11am", "12md", "1pm", "2pm", "4pm"],
    },
    "yAxis": {"type": "value"},
    "series": [{"data": [validos2023*0.1, validos2023*0.2, validos2023*0.35, validos2023*0.5, validos2023*0.75, validos2023*0.9, validos2023], "type": "line"}],
}
st_echarts(
    options=option, height="400px",
)

st.header("Proyección con Escenario Histórico Retador (18,5% crecimiento votos y 39% participación para victoria):")
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

st.write("De modo que se requerirían 84.000 votos. Ahora bien, si el crecimiento de los votos válidos no fuera del 18% sino del 12%, la votación necesaria sería de 80.000 votos")
st.write("Un escenario más competido sería en el que para ganar se requiera el 33% de los votos válidos, para lo cual se requerirían 71.550 votos asumiendo crecimiento promedio de 18,85% de los votos válidos")
st.write("Pero si los votos válidos no crecen al 18,85% sino al 12% y la participación pa ganar fuese del 33%, los votos mínimos serían de 67429")
st.write("Sin embargo, la migración venezolana permite intuir que el crecimiento de los votos válidos no se desacelerará con fuerza e incluso se puede mantener el ritmo promedio del 18,8%")


st.title("3. Requisitos para ganar al 36% de participación: 77.499 🗳️")
meta2023 = validos2023*0.36
st.write('El ritmo de votos requeridos por la campaña por hora es de: ', meta2023/8)  
st.write('El ritmo de votos requeridos por la campaña por minuto es de: ', meta2023/480)
meta_zona_1 = 10290
meta_zona_2 = 11986
meta_zona_3 = 11368
meta_zona_4 = 14018
meta_zona_5 = 14036
meta_zona_6 = 5241
meta_zona_7 = 3112
meta_zona_8 = 110
meta_zona_9 = 7338
st.markdown(
  """
  🗳️ Votación requerida ponderada por zonas:
  - Zona 1: _    10290 🗳️
  - Zona 2: _    11986 🗳️
  - Zona 3: _    11368 🗳️
  - Zona 4: _    14018 🗳️
  - Zona 5: _    14036 🗳️
  - Zona 6: _    5241 🗳️
  - Zona 7: _    3112 🗳️
  - Zona 8: _    110 🗳️
  - Zona 9: _    7338 🗳️
  
  Todo lo anterior con el siguiente ritmo de votación hora a hora 🕰:
  """
)
st.header('Votos requeridos por zonas para ganar Alcaldía Valledupar 2023')
options = {
            "title": {"text": "Votos x Zonas"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
            },
            "legend": {"data": ["Zona_9", "Zona_8", "Zona_7", "Zona_6", "Zona_5", "Zona_4", "Zona_3", "Zona_2", "Zona_1"]},
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": ["10am", "11am", "12md", "1pm", "2pm", "3pm", "4pm"],
                }
            ],
            "yAxis": [{"type": "value"}],
            "series": [
                {
                    "name": "Zona_9",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_9*0.1, meta_zona_9*0.2, meta_zona_9*0.35, meta_zona_9*0.45, meta_zona_9*0.5, meta_zona_9*0.75, meta_zona_9],
                },
                {
                    "name": "Zona_8",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_8*0.1, meta_zona_8*0.2, meta_zona_8*0.35, meta_zona_8*0.45, meta_zona_8*0.5, meta_zona_8*0.75, meta_zona_8],
                },
                {
                    "name": "Zona_7",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_7*0.1, meta_zona_7*0.2, meta_zona_7*0.35, meta_zona_7*0.45, meta_zona_7*0.5, meta_zona_7*0.75, meta_zona_7],
                },
                  {
                    "name": "Zona_6",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_6*0.1, meta_zona_6*0.2, meta_zona_6*0.35, meta_zona_6*0.45, meta_zona_6*0.5, meta_zona_6*0.75, meta_zona_6],
                },
                 {
                    "name": "Zona_5",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                },
                  {
                    "name": "Zona_4",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                },
                  {
                    "name": "Zona_3",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                },
                  {
                    "name": "Zona_2",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                },
                  {
                    "name": "Zona_1",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                },
            ],
        }
st_echarts(options=options, height="400px") 


st.write('Ritmo de votación por generos requerido')
st.header("Votos requeridos por género para ganar Alcaldía Valledupar 2023 en escenario histórico")
st.subheader("Suponiendo crecimiento electoral del 18% y participación de victoria del 39%")
st.write("Mujeres: 43.378 ; Hombres: 41.180")
option = {
    "legend": {},
    "tooltip": {"trigger": "axis", "showContent": False},
    "dataset": {
        "source": [
            ["product", "Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5", "Zona 6", "Zona 7", "Zona 8", "Zona 9"],
            ["Mujer", 5760, 6709, 6363, 7846, 7856, 2934, 1742, 61, 4108],
            ["Hombre", 5468, 6369, 6041, 7448, 7458, 2785, 1654, 58, 3899],
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
            "type": "pie",
            "id": "pie",
            "radius": "30%",
            "center": ["50%", "25%"],
            "emphasis": {"focus": "data"},
            "label": {"formatter": "{b}: {@2012} ({d}%)"},
            "encode": {"itemName": "product", "value": "Zona 9", "tooltip": "Zona 9"},
        },
    ],
}
st_echarts(option, height="500px", key="echarts")

st.write('Ritmo de votación por edades requerido')




st.write('---')



st.write('---')


st.header('Zona 1 - Puestos de Votación 🗳️')

zona_1 = pd.DataFrame({
   'lon':[10.473583, 10.474139, 10.478472, 10.468500, 10.469667, 10.474139],
   'lat':[-73.248639, -73.25125, -73.245361, -73.247278, -73.238056, -73.25125],
   'name':['PV1 COL. Nacional Loperena', 'PV2 ESC Bellas Artes', 'PV3 UDES', 'PV4 COL Prudencia Daza', 'PV5 COL SantoDomingo', 'PV6 COL Parroquial El Carmelo'],
   'value':[7588, 4933,3771, 2735, 5666, 57]
}, dtype=str)


st.write('Georreferenciación por Puestos de Votación Zona 1 y 2 - Con mapas Folium')
# center on Liberty Bell, add marker
m = folium.Map(location=[10.4735, -73.2486], zoom_start=13)
#zona1
folium.Marker(
    [10.47358, -73.248639], popup="PV1 COL Nacional Loperena", tooltip="PV1 COL Nacional Loperena"
).add_to(m)
folium.Marker(
    [10.474139, -73.25125], popup="PV2 ESC Bellas Artes", tooltip="PV2 ESC Bellas Artes"
).add_to(m)
folium.Marker(
    [10.478472, -73.245361], popup="PV3 UDES", tooltip="PV3 UDES"
).add_to(m)
folium.Marker(
    [10.468500, -73.247278], popup="PV4 COL Prudencia Daza", tooltip="PV4 COL Prudencia Daza"
).add_to(m)
folium.Marker(
    [10.469667, -73.238056], popup="PV5 COL SantoDomingo", tooltip="PV5 COL SantoDomingo"
).add_to(m)
folium.Marker(
    [10.474130, -73.251115], popup="PV6 COL Parroquial El Carmelo (Nuevo 2023)", tooltip="PV6 COL Parroquial El Carmelo"
).add_to(m)
#zona2
folium.Marker(
    [10.46006, -73.22889], popup="Z2 PV1 PV7 COL Francisco Molina Sanchez", tooltip="Z2 PV1 PV7 COL Francisco Molina Sanchez"
).add_to(m)
folium.Marker(
    [10.46322, -73.23575], popup="Z2 PV2 PV8 I.E. Manuel Germán Cuello", tooltip="Z2 PV1 PV8 I.E. Manuel Germán Cuello"
).add_to(m)
folium.Marker(
    [10.45389, -73.24211], popup="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña", tooltip="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña"
).add_to(m)
folium.Marker(
    [10.45100, -73.23672], popup="Z2 PV4 PV10 UNV. Abierta y a Distancia", tooltip="Z2 PV4 PV10 UNV. Abierta y a Distancia"
).add_to(m)

st_data = st_folium(m, width=725)



