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



st.header("Cronograma de Interacciones por Equipos")
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Líderes", "Mail Ad", "Affiliate Ad", "Video Ad", "Search Engine"]
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
            "name": "Mail Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [120, 132, 101, 134, 90, 230, 210],
        },
        {
            "name": "Affiliate Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "Video Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [150, 212, 201, 154, 190, 330, 410],
        },
        {
            "name": "Search Engine",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [820, 832, 901, 934, 1290, 1330, 1320],
        },
    ],
}
st_echarts(options=options, height="500px")
          
          
          
