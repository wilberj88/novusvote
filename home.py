import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Mandos para Campañas Electorales Exitosas")

st.write("""
**Uno por cada etapa de tu campaña:**
- 🗳️: `PRE CAMPAÑA: metas y requisitos`
- 🧑‍⚖️: `CAMPAÑA: necesidades y soluciones`
- 💲: `DÍA ELECTORAL: cronograma y monitoreo`
- 🧭: `POST CAMPAÑA: resultados, mensajes por territorios y próximos pasos`
""")

if st.button('Calcular diagnóstico gratuito'):
    st.header("Indícanos tu meta y te diremos todo lo que requieres")
    meta = st.slider('¿Cuántos votos estimas necesitar para posecionarte?', 0, 100000)
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
