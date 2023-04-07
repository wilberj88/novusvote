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
st.title('¿Cuál es la meta de la campaña electoral?')
meta = st.slider('¿Cuántos votos necesitas para posecionarte?', 0, 300000)
#meta = st.number_input('Ingresa la META DE VOTACIÓN del candidat@', min_value=1000, max_value=100000, value=10000)
if meta:
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
        
        st.title('Votación Requerida por Localidades más Pobladas')
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
        
        st.title('Ritmo de votación por hora requerido')
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
        st.write('El ritmo de votos requeridos por minuto es de: ', meta/480)
        st.write('El ritmo de votos requeridos por hora es de: ', meta/8)
        st.title('Probabilidad Promedio de Éxito')
        liquidfill_option = {
            "series": [{"type": "liquidFill", "data": [0.6, 0.5, 0.4, 0.3]}]
        }
        st_echarts(liquidfill_option)

        
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
                        "data": [{"value": 25, "name": "Concejales"}],
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
               


                ST_HEATMAP_DEMOS = {
                    "Heatmap: Heatmap Cartesian": (
                        render_heatmap_cartesian,
                        "https://echarts.apache.org/examples/en/editor.html?c=heatmap-cartesian",
                    ),
                }

                render_heatmap_cartesian()
              
                
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




