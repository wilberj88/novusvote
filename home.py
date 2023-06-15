import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts
from streamlit_timeline import st_timeline
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64
from pyecharts import options as opts
from pyecharts.charts import Graph
#import streamlit.components.v1 as components
#import bar_chart_race as bcr


st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Tecnología Electoral", page_icon="🗳️")

st.title('Novus Vote 🗳️')

st.header("Tecnología para Campañas Electorales Exitosas")
st.write("_Si no te hacemos ganar, te diremos exactamente dónde y por qué perdiste_")

st.write("Son 4 etapas y 4 ritmos distintos: Pre Campaña + Campaña + Día Elección + Post Campaña ")

items = [
    {"id": 1, "content": "2023-06-15", "start": "2023-07-29"},
    {"id": 2, "content": "2023-10-21", "start": "2023-07-30"},
    {"id": 3, "content": "2023-11-06", "start": "2023-10-22"},
    {"id": 4, "content": "2023-11-07", "start": "2024-01-30"},
]

#items = [
#    {"id": 1, "PRE Campaña inicia:": "2023-06-15", "PRE Campaña finaliza:": "2023-07-29"},
#    {"id": 2, "Campaña inicia:": "2023-07-29", "Campaña finaliza": "2023-10-21"},
#    {"id": 3, "Día E inicia:": "2023-10-22", "Día E finalizada:": "2023-11-06"},
#    {"id": 4, "POST Campaña inicia": "2022-10-16", "POST Campaña finaliza": "2022-10-16"},
#]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)




st.title("Test Plan")

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


if 'timeline' not in st.session_state:
    st.session_state['timeline'] = None
    st.session_state['timeline_items'] = [
        {"id": 1, "content": "static 1", "start": "2022-10-20"},
        {"id": 2, "content": "Editable 1", "start": "2022-10-09", "editable": True},
        {"id": 3, "content": "Editable 2", "start": "2022-10-18", "editable": True},
        {"id": 4, "content": "static 2", "start": "2022-10-16"},
        {"id": 5, "content": "static 3", "start": "2022-10-25"},
        {"id": 6, "content": "static 4", "start": "2022-10-27"},
    ]


def display_return_info(place):
    with place:
        with st.container():
            st.title('Returned value:')
            st.write(st.session_state['timeline'])


def run_code():
    st.title("Streamlit Timeline")
    timeline_form = st.form(key='foo')
    return_vals = st.empty()

    with timeline_form:
        timeline = st_timeline(st.session_state['timeline_items'], groups=[], options={}, height="300px")
        if st.form_submit_button('Done'):
            st.session_state['timeline'] = timeline
            display_return_info(return_vals)


run_code()


st.write('---')
st.title("Población con mayor Participación Electoral")
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
            "name": "Los más votadores",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 40, "name": "Hombre35-45"},
                {"value": 38, "name": "Mujeres55-65"},
                {"value": 32, "name": "Jóvenes18-25"},
                {"value": 30, "name": "Trabajador30-45"},
                {"value": 28, "name": "Funcionario30-65"},
                {"value": 26, "name": "Deportistas20-60"},
                {"value": 22, "name": "Religiosos50-75"},
                {"value": 18, "name": "Universitarios-18-32"},
            ],
        }
    ],
}
st_echarts(
    options=option, height="600px",
)
st.write('---')



st.title("Votación histórica por partidos o ideologías")
option = {
    "legend": {},
    "tooltip": {"trigger": "axis", "showContent": False},
    "dataset": {
        "source": [
            ["product", "1999", "2004", "2007", "2011", "2015", "2019"],
            ["Conservador", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
            ["Verde", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
            ["Polo", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
            ["Liberal", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
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
            "encode": {"itemName": "product", "value": "2019", "tooltip": "2019"},
        },
    ],
}
st_echarts(option, height="500px", key="echarts")
st.write('---')


st.header("Interacciones diarias por Equipos")
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Líderes", "Voluntarios", "Testigos", "Defensores", "Logística"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "series": [
        {
            "name": "Líderes",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [320, 302, 301, 334, 390, 330, 320],
        },
        {
            "name": "Voluntarios",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [120, 132, 101, 134, 90, 230, 210],
        },
        {
            "name": "Testigos",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "Defensores",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [150, 212, 201, 154, 190, 330, 410],
        },
        {
            "name": "Logística",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [820, 832, 901, 934, 1290, 1330, 1320],
        },
    ],
}
st_echarts(options=options, height="500px")
          
st.write('---')
    

st.title("Palabras clave por Barrio")
data = [
    {"name": name, "value": value}
    for name, value in [
        ("Trabajo", "999"),
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
        ("Seguridad", "406"),
        ("Crimen", "386"),
        ("Secuestros", "385"),
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

    
st.header("Cronograma de publicaciones en Redes")
def render_heatmap_cartesian():
    hours = [
        "12a",
        "1a",
        "2a",
        "3a",
        "4a",
        "5a",
        "6a",
        "7a",
        "8a",
        "9a",
        "10a",
        "11a",
        "12p",
        "1p",
        "2p",
        "3p",
        "4p",
        "5p",
        "6p",
        "7p",
        "8p",
        "9p",
        "10p",
        "11p",
    ]
    days = [
        "Saturday",
        "Friday",
        "Thursday",
        "Wednesday",
        "Tuesday",
        "Monday",
        "Sunday",
    ]

    data = [
        [0, 0, 5],
        [0, 1, 1],
        [0, 2, 0],
        [0, 3, 0],
        [0, 4, 0],
        [0, 5, 0],
        [0, 6, 0],
        [0, 7, 0],
        [0, 8, 0],
        [0, 9, 0],
        [0, 10, 0],
        [0, 11, 2],
        [0, 12, 4],
        [0, 13, 1],
        [0, 14, 1],
        [0, 15, 3],
        [0, 16, 4],
        [0, 17, 6],
        [0, 18, 4],
        [0, 19, 4],
        [0, 20, 3],
        [0, 21, 3],
        [0, 22, 2],
        [0, 23, 5],
        [1, 0, 7],
        [1, 1, 0],
        [1, 2, 0],
        [1, 3, 0],
        [1, 4, 0],
        [1, 5, 0],
        [1, 6, 0],
        [1, 7, 0],
        [1, 8, 0],
        [1, 9, 0],
        [1, 10, 5],
        [1, 11, 2],
        [1, 12, 2],
        [1, 13, 6],
        [1, 14, 9],
        [1, 15, 11],
        [1, 16, 6],
        [1, 17, 7],
        [1, 18, 8],
        [1, 19, 12],
        [1, 20, 5],
        [1, 21, 5],
        [1, 22, 7],
        [1, 23, 2],
        [2, 0, 1],
        [2, 1, 1],
        [2, 2, 0],
        [2, 3, 0],
        [2, 4, 0],
        [2, 5, 0],
        [2, 6, 0],
        [2, 7, 0],
        [2, 8, 0],
        [2, 9, 0],
        [2, 10, 3],
        [2, 11, 2],
        [2, 12, 1],
        [2, 13, 9],
        [2, 14, 8],
        [2, 15, 10],
        [2, 16, 6],
        [2, 17, 5],
        [2, 18, 5],
        [2, 19, 5],
        [2, 20, 7],
        [2, 21, 4],
        [2, 22, 2],
        [2, 23, 4],
        [3, 0, 7],
        [3, 1, 3],
        [3, 2, 0],
        [3, 3, 0],
        [3, 4, 0],
        [3, 5, 0],
        [3, 6, 0],
        [3, 7, 0],
        [3, 8, 1],
        [3, 9, 0],
        [3, 10, 5],
        [3, 11, 4],
        [3, 12, 7],
        [3, 13, 14],
        [3, 14, 13],
        [3, 15, 12],
        [3, 16, 9],
        [3, 17, 5],
        [3, 18, 5],
        [3, 19, 10],
        [3, 20, 6],
        [3, 21, 4],
        [3, 22, 4],
        [3, 23, 1],
        [4, 0, 1],
        [4, 1, 3],
        [4, 2, 0],
        [4, 3, 0],
        [4, 4, 0],
        [4, 5, 1],
        [4, 6, 0],
        [4, 7, 0],
        [4, 8, 0],
        [4, 9, 2],
        [4, 10, 4],
        [4, 11, 4],
        [4, 12, 2],
        [4, 13, 4],
        [4, 14, 4],
        [4, 15, 14],
        [4, 16, 12],
        [4, 17, 1],
        [4, 18, 8],
        [4, 19, 5],
        [4, 20, 3],
        [4, 21, 7],
        [4, 22, 3],
        [4, 23, 0],
        [5, 0, 2],
        [5, 1, 1],
        [5, 2, 0],
        [5, 3, 3],
        [5, 4, 0],
        [5, 5, 0],
        [5, 6, 0],
        [5, 7, 0],
        [5, 8, 2],
        [5, 9, 0],
        [5, 10, 4],
        [5, 11, 1],
        [5, 12, 5],
        [5, 13, 10],
        [5, 14, 5],
        [5, 15, 7],
        [5, 16, 11],
        [5, 17, 6],
        [5, 18, 0],
        [5, 19, 5],
        [5, 20, 3],
        [5, 21, 4],
        [5, 22, 2],
        [5, 23, 0],
        [6, 0, 1],
        [6, 1, 0],
        [6, 2, 0],
        [6, 3, 0],
        [6, 4, 0],
        [6, 5, 0],
        [6, 6, 0],
        [6, 7, 0],
        [6, 8, 0],
        [6, 9, 0],
        [6, 10, 1],
        [6, 11, 0],
        [6, 12, 2],
        [6, 13, 1],
        [6, 14, 3],
        [6, 15, 4],
        [6, 16, 0],
        [6, 17, 0],
        [6, 18, 0],
        [6, 19, 0],
        [6, 20, 1],
        [6, 21, 2],
        [6, 22, 2],
        [6, 23, 6],
    ]
    data = [[d[1], d[0], d[2] if d[2] != 0 else "-"] for d in data]

    option = {
        "tooltip": {"position": "top"},
        "grid": {"height": "50%", "top": "10%"},
        "xAxis": {"type": "category", "data": hours, "splitArea": {"show": True}},
        "yAxis": {"type": "category", "data": days, "splitArea": {"show": True}},
        "visualMap": {
            "min": 0,
            "max": 10,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "15%",
        },
        "series": [
            {
                "name": "Punch Card",
                "type": "heatmap",
                "data": data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
            }
        ],
    }
    st_echarts(option, height="500px")


ST_HEATMAP_DEMOS = {
    "Heatmap: Heatmap Cartesian": (
        render_heatmap_cartesian,
        "https://echarts.apache.org/examples/en/editor.html?c=heatmap-cartesian",
    ),
}

render_heatmap_cartesian()
 

st.write('---')

st.title("Votos requeridos por Segmentos Poblacionales")
options = {
    "title": {"text": "Votos por Edades", "subtext": "Décadas", "left": "center"},
    "tooltip": {"trigger": "item"},
    "legend": {
        "orient": "vertical",
        "left": "left",
    },
    "series": [
        {
            "name": "Votos para ganar en 2023",
            "type": "pie",
            "radius": "50%",
            "data": [
                {"value": 1048, "name": "+60años"},
                {"value": 735, "name": "50-60años"},
                {"value": 580, "name": "40-50años"},
                {"value": 484, "name": "30-40años"},
                {"value": 300, "name": "18-30años"},
            ],
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                }
            },
        }
    ],
}
st.markdown("Selecciona y analiza detalles")
events = {
    "legendselectchanged": "function(params) { return params.selected }",
}
s = st_echarts(
    options=options, events=events, height="600px", key="render_pie_events"
)
if s is not None:
    st.write(s)

    
    
st.write('---')
st.title("Conversión de Votantes por Barrio")
    
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
    

        
    
st.write('---')
st.title("Predicción de votos por Bario y Mesa de Votación")
option = {
    "xAxis": {"data": ["Norte", "Sur", "Oriente", "Occidente"]},
    "yAxis": {},
    "series": [
        {
            "type": "k",
            "data": [
                [20, 34, 10, 38],
                [40, 35, 30, 50],
                [31, 38, 33, 44],
                [38, 15, 5, 42],
            ],
        }
    ],
}
st_echarts(option, height="500px")

        
    
st.write('---')
st.title("Actualizaciones de Resultados Electorales")
#df = bcr.load_dataset("covid19_tutorial")
#html_str = bcr.bar_chart_race(df=df).data

#start = html_str.find('base64,')+len('base64,')
#end = html_str.find('">')

#video = base64.b64decode(html_str[start:end])
#st.video(video)        
    
st.write('---')
