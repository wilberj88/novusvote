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

st.title('PRE CAMPAÑA - Históricos y Proyecciones a domingo 29 de Octubre de 2023')
st.header("Históricos: Datos procesados 🛠️")
columnas_to_keep = ["Nombre", "Votos Válidos 2019", "Latitud", "Longitud"]
data = pd.read_csv('pages/datos/Votos Válidos procesados Valledupar 2015-2019 - Puro Puestos.csv', usecols=columnas_to_keep)
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


st.title("Top 3 entre 2015 y 2019")
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

st.write('--')

st.header('Zona 1 - Puestos de Votación 🗳️')
st.write('Con mapas PyDeck')

st.pydeck_chart(pdk.Deck(
map_style=None,
initial_view_state=pdk.ViewState(
latitude=10.47,
longitude=-73.24,
zoom=11,
pitch=10,
),
layers=[
pdk.Layer(
   'HexagonLayer',
   data = data_pura,
   get_position='[Longitud, Latitud]',
   radius = 200,
   elevation_scale = '[Votos Válidos 2019]',
   elevation_range = [0, 11000],
   pickable = True,
   extruded = True,
),
pdk.Layer(
    'ScatterplotLayer',
    data = data_pura,
    get_position='[Longitud, Latitud]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
),
],
))    


st.write('Con mapas Folium')
# center on Liberty Bell, add marker
m = folium.Map(location=[10.473583, -73.248639], zoom_start=14)
folium.Marker(
    [10.473583, -73.248639], popup="PV1 COL NAL Loperena", tooltip="PV1 COL NAL Loperena"
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
#folium.Marker(
#    [10.474139, -73.25125], popup="PV6 COL Parroquial El Carmelo", tooltip="PV6 COL Parroquial El Carmelo"
#).add_to(m)
# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)




st.write('---')

st.header("Proyecciones para ganar en Octubre de 2023")
st.write('El crecimiento de los votos válidos entre 2015 y 2019 fue en promedio de 18%, siendo la zona 5 la de mayor crecimiento (35%) y la zona 7 la de mayor contracción (-13%)')
st.write('Asumiendo que se requiere un 39% de los votos para ganar y que el crecimiento promedio desde hace 8 años en los votos válidos es de un 18%, los resultados son: ')

votos_validos = pd.DataFrame(
    {
        "2015": [153508],
        "2019": [182437],
        "2023": ["?"],
    }
)
st.dataframe(votos_validos)

st.write("Votos válidos proyectados por zonas")
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
                {"value": 28789, "name": "Zona 1 (13,3%)"},
                {"value": 33532, "name": "Zona 2 (15,5%)"},
                {"value": 31805, "name": "Zona 3 (14,7%)"},
                {"value": 39217, "name": "Zona 4 (18,1%)"},
                {"value": 39268, "name": "Zona 5 (18,1%)"},
                {"value": 14663, "name": "Zona 6 (6,8%)"},
                {"value": 8707, "name": "Zona 7 (4%)"},
                {"value": 307, "name": "Zona 8 (0,1%)"},
                {"value": 20531, "name": "Zona 9 (9,5%)"},
            ],
        }
    ],
}
st_echarts(
    options=option, height="600px",
)
st.write("De modo que se requerirían 84.000 votos. Ahora bien, si el crecimiento de los votos válidos no fuera del 18% sino del 12%, la votación necesaria sería de 80.000 votos")
st.write("Un escenario más competido sería en el que para ganar se requiera el 33% de los votos válidos, para lo cual se requerirían 71.550 votos asumiendo crecimiento promedio de 18,85% de los votos válidos")
st.write("Pero si los votos válidos no crecen al 18,85% sino al 12% y la participación pa ganar fuese del 33%, los votos mínimos serían de 67429")
st.write("Sin embargo, la migración venezolana permite intuir que el crecimiento de los votos válidos no se desacelerará con fuerza e incluso se puede mantener el ritmo promedio del 18,8%")
st.write('---')
st.header("Votos requeridos por zonas para ganar Alcaldía 2023 (18,5% crecimiento votos y 39% participación para victoria)")
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
st.header("Votos requeridos por género para ganar Alcaldía 2023")
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

st.write('---')
st.header("Votos requeridos por edades para ganar Alcaldía 2023")

st.header("Modelador de escenarios")


st.write('---')
st.header('Conclusiones PRE CAMPAÑA - Tareas Campaña')
meta = 84558
st.write('Votos mínimos para aspirar a posesionarse Alcalde de Valledupar: entre 67.429 con desaceleración del crecimiento y hasta', meta) 
st.write('Ritmo de votos mínimos por hora para aspirar a posesionarse Alcalde de Valledupar:', meta/8) 
st.write('Ritmo de votos mínimos por minuto para aspirar a posesionarse Alcalde de Valledupar:', meta/480) 
st.write('Importancia de Zonas por Votos: Zona 5 > Zona 4 > Zona 2 > Zona 3 > Zona 1 > Zona 9 > Zona 6 > Zona 7 > Zona 8')

st.write('---')
