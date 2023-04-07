import streamlit as st
from streamlit_echarts import st_echarts
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
meta = st.slider('¿Cuál es la meta de votos?', 0, 300000)
#meta = st.number_input('Ingresa la META DE VOTACIÓN del candidat@', min_value=1000, max_value=100000, value=10000)
if meta:
        st.write('El ritmo de votos por minuto es de: ', meta/4800)
        st.write('El ritmo de votos por hora es de: ', meta/8)
        
        
        option = {
            "xAxis": {
                "type": "category",
                "data": ["9am", "10am", "11am", "12md", "1pm", "2pm", "4pm"],
            },
            "yAxis": {"type": "value"},
            "series": [{"data": [meta*0.1, meta*0.2, meta*0.35, meta*0.5, meta*0.75, meta*0.9, meta], "type": "line"}],
        }
        st_echarts(
            options=option, height="400px",
        )
        
        
        st.write("ALARMA de desempeño requerido para minimizar riesgo y obtener la meta de votación 🗳️")

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
                        "data": [{"value": 99, "name": "Firmas"}],
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
                        "data": [{"value": 80, "name": "Votos"}],
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
                        "data": [{"value": 66, "name": "Sentimiento"}],
                    }
                ],
            }
          st_echarts(options=acelerometro3)

        territorio = st.selectbox("Indica el Territorio",
        ("Bogotá", "Medellín", "Cali", "Bucaramanga", "Barrancabermeja"),
        )
        categoria = st.radio(
        "Indica la categoría de campaña👇 ",
        options=['Gobernación', 'Asamblea Departamental','Alcaldía', 'Concejo', 'Junta de Acción Comunal'],
        )
        if territorio and categoria:
                st.write('Votos máximos individuales en la circunscripción:', meta*2) 
             
                st.write('RECOMENDACIÓN de ritmo de votación por Top7 localidades más densas:')
                def render_heatmap_cartesian():
                    hours = [
                        "8a",
                        "9a",
                        "10a",
                        "11a",
                        "12p",
                        "1p",
                        "2p",
                        "3p",
                        "4p",
                    ]
                    days = [
                        "Localidad 1",
                        "Localidad 2",
                        "Localidad 3",
                        "Localidad 4",
                        "Localidad 5",
                        "Localidad 6",
                        "Localidad 7",
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
                st.title('Votos requeridos por Localidades Top5 más pobladas')
                options = {
                    "title": {"text": "Votos x Zonas"},
                    "tooltip": {
                        "trigger": "axis",
                        "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
                    },
                    "legend": {"data": ["LocalidadTop5", "LocalidadTop4", "LocalidadTop3", "LocalidadTop2", "LocalidadTop1"]},
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
                            "name": "LocalidadTop5",
                            "type": "line",
                            "stack": "总量",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            "data": [meta*0.01, meta*0.02, meta*0.035, meta*0.045, meta*0.05, meta*0.065, meta*0.07],
                        },
                        {
                            "name": "LocalidadTop4",
                            "type": "line",
                            "stack": "总量",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            "data": [meta*0.05, meta*0.06, meta*0.07, meta*0.08, meta*0.09, meta*0.10, meta*0.16],
                        },
                        {
                            "name": "LocalidadTop3",
                            "type": "line",
                            "stack": "总量",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            "data": [meta*0.02, meta*0.04, meta*0.06, meta*0.08, meta*0.1, meta*0.12, meta*0.21],
                        },
                        {
                            "name": "LocalidadTop2",
                            "type": "line",
                            "stack": "总量",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            "data": [meta*0.07, meta*0.08, meta*0.09, meta*0.11, meta*0.13, meta*0.16, meta*0.25],
                        },
                        {
                            "name": "LocalidadTop1",
                            "type": "line",
                            "stack": "总量",
                            "label": {"show": True, "position": "top"},
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            "data": [meta*0.08, meta*0.12, meta*0.15, meta*0.2, meta*0.25, meta*0.28, meta*0.31],
                        },
                    ],
                }
                st_echarts(options=options, height="400px")
                
                st.title('Probabilidad Promedio de Éxito')
                liquidfill_option = {
                    "series": [{"type": "liquidFill", "data": [0.6, 0.5, 0.4, 0.3]}]
                }
                st_echarts(liquidfill_option)
                
                st.title('Alianzas Requeridas')
                nodes = [
                    {"name": "Consejal 1", "symbolSize": 10},
                    {"name": "Consejal 2", "symbolSize": 20},
                    {"name": "Consejal 3", "symbolSize": 30},
                    {"name": "Consejal 4", "symbolSize": 40},
                    {"name": "Consejal 5", "symbolSize": 50},
                    {"name": "Consejal 6", "symbolSize": 40},
                    {"name": "Consejal 7", "symbolSize": 30},
                    {"name": "Consejal 8", "symbolSize": 20},
                ]
                links = []
                for i in nodes:
                    for j in nodes:
                        links.append({"source": i.get("name"), "target": j.get("name")})
                c = (
                    Graph()
                    .add("", nodes, links, repulsion=8000)
                    .set_global_opts(title_opts=opts.TitleOpts(title="Grafos"))
                )
                st_pyecharts(c)




