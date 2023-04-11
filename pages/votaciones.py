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


#CONFIGURACIÓN DEL MANDO
st.title('¿Cuál es la meta de la campaña electoral?')
territorio = st.selectbox("Indica el Territorio",
("Bogotá", "Medellín", "Cali", "Bucaramanga", "Barrancabermeja"),
)
categoria = st.radio(
"Indica la categoría de campaña👇 ",
options=['Gobernación', 'Asamblea Departamental','Alcaldía', 'Concejo', 'Junta de Acción Comunal'],
)
meta = st.slider('¿Cuántos votos estimas necesitar para posecionarte?', 0, 300000)
#meta = st.number_input('Ingresa la META DE VOTACIÓN del candidat@', min_value=1000, max_value=100000, value=10000)
if meta:     
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
        
        st.title("Desagregación de votos por barrios de acuerdo con las votaciones históricas")
        #datos
        df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [4.2620, -75.13],
        columns=['lat', 'lon'])
        st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
        latitude=4.26,
        longitude=-75.13,
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
        
        st.title("Líderes necesarios para votación mínima")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.area_chart(chart_data)
        
        st.title("Financiación necesaria")
        # Add histogram data
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

        # Group data together
        hist_data = [x1, x2, x3]

        group_labels = ['Group 1', 'Group 2', 'Group 3']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

        # Plot!
        st.plotly_chart(fig, use_container_width=True)
        
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

        st.title('Diagnóstico y Contraste de Competencia Actual y Previa')
        def render_basic_radar():
            option = {
                "title": {"text": "Previo Votación 🗳️"},
                "legend": {"data": ["Candidato A", "Candidato B"]},
                "radar": {
                    "indicator": [
                        {"name": "Líderes", "max": 6500},
                        {"name": "Financiación", "max": 16000},
                        {"name": "Sentimiento", "max": 30000},
                        {"name": "Votación Anterior", "max": 38000},
                        {"name": "Interaciones", "max": 52000},
                        {"name": "Recordación de Marca", "max": 25000},
                    ]
                },
                "series": [
                    {
                        "name": "Aprendizaje Actual Vs Proyectado",
                        "type": "radar",
                        "data": [
                            {
                                "value": [2000, 10000, 20000, 3500, 15000, 11800],
                                "name": "Candidato A",
                            },
                            {
                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                "name": "Candidato B",
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
        
        st.title("Probabilidades de Riesgos Climáticos para la Jornada Electoral 🌧️🗳️🌧️")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Llovizna", "70%", "40%")
        col2.metric("Lluvia", "50%", "-82%")
        col3.metric("Tormenta", "36%", "43%")
        col4.metric("Diluvio", "7%", "78%")
        
        st.title('Probabilidad de Éxito con Financiacion Completa 💰🗳️💰')
        liquidfill_option = {
            "series": [{"type": "liquidFill", "data": [0.6, 0.5, 0.4, 0.3]}]
        }
        st_echarts(liquidfill_option)
        st.write('Votos máximos individuales en la circunscripción:', meta*2) 
    
        st.title("ALARMAS de desempeño requerido para minimizar riesgo y obtener la meta de votación 🗳️")
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
                        "data": [{"value": 90, "name": "Votos"}],
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

       
    
             
            
