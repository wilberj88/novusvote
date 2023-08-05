import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote - Diego Molano Aponte", page_icon="🗳️")


# Add a title and intro text
st.title('Novus Vote 🗳️ Bogotá PreCampaña - Diego Molano')
st.title('Votación histrórica en Bogotá por localidades')
st.header('Votos Uribistas al Congreso y Presidencia 2018')
def render_basic_radar():
    option = {
        "title": {"text": "🗳️"},
        "legend": {"data": ["CD_Cámara_2018", "CD_Senado_2018", "CD_Presi_2018_1", "CD_Presi_2018_2"]},
        "radar": {
            "indicator": [
                {"name": "Usaquén", "max": 142000},
                {"name": "Chapinero", "max": 142000},
                {"name": "SantaFé", "max": 142000},
                {"name": "SanCristobal", "max": 142000},
                {"name": "Usme", "max": 142000},
                {"name": "Tunjuelito", "max": 142000},
                {"name": "Bosa", "max": 142000},
                {"name": "Kennedy", "max": 142000},
                {"name": "Fontibon", "max": 142000},
                {"name": "Engativá", "max": 142000},
                {"name": "Suba", "max": 142000},
                {"name": "BarriosUnidos", "max": 142000},
                {"name": "Teusaquillo", "max": 142000},
                {"name": "Mártires", "max": 142000},
                {"name": "A.Nariño", "max": 142000},
                {"name": "PuenteAranda", "max": 142000},
                {"name": "Candelaria", "max": 142000},
                {"name": "RafaelUribe", "max": 142000},
                {"name": "C.Bolivar", "max": 142000},
                {"name": "Sumapaz", "max": 142000},
            ]
        },
        "series": [
            {
                "name": "Votos por Zonas",
                "type": "radar",
                "data": [
                    {
                        "value": [41805, 16516, 3910, 10960, 8972, 7507, 16577, 32557, 14405, 33250, 50312, 11049, 12849, 4926, 6157, 13816, 1934, 12890, 17193, 20],
                        "name": "CD_Cámara_2018",
                    },
                    {
                        "value": [49000, 19427, 4611, 13228, 10880, 9156, 20217, 39371, 17536, 40024, 59549, 13251, 15500, 5809, 7469, 16524, 2272, 15375, 20168, 44],
                        "name": "CD_Senado_2018",
                    },
                    {
                        "value": [52074, 19291, 7167, 22504, 21263, 14697, 35214, 62239, 23970, 54691, 71106, 15821, 16495, 9196, 11073, 23476, 3367, 25318, 38290, 156],
                        "name": "CD_Presi_2018_1",
                    },
                    {
                        "value": [93918, 32843, 14102, 47474, 42737, 29908, 71009, 125169, 47346, 113650, 141800, 31327, 31295, 16813, 21321, 45782, 6591, 50580, 75825, 256],
                        "name": "CD_Presi_2018_2",
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


st.header('Votos Aspirantes Alcaldía Bog 2019')
def render_basic_radar():
    option = {
        "title": {"text": "🗳️"},
        "legend": {"data": ["Hollman", "Claudia", "Galán", "MiguelU"]},
        "radar": {
            "indicator": [
                {"name": "Usaquén", "max": 162000},
                {"name": "Chapinero", "max": 162000},
                {"name": "SantaFé", "max": 162000},
                {"name": "SanCristobal", "max": 162000},
                {"name": "Usme", "max": 162000},
                {"name": "Tunjuelito", "max": 162000},
                {"name": "Bosa", "max": 162000},
                {"name": "Kennedy", "max": 162000},
                {"name": "Fontibon", "max": 162000},
                {"name": "Engativá", "max": 162000},
                {"name": "Suba", "max": 162000},
                {"name": "BarriosUnidos", "max": 162000},
                {"name": "Teusaquillo", "max": 162000},
                {"name": "Mártires", "max": 162000},
                {"name": "A.Nariño", "max": 162000},
                {"name": "PuenteAranda", "max": 162000},
                {"name": "Candelaria", "max": 162000},
                {"name": "RafaelUribe", "max": 162000},
                {"name": "C.Bolivar", "max": 162000},
                {"name": "Sumapaz", "max": 162000},
            ]
        },
        "series": [
            {
                "name": "Votos por Zonas",
                "type": "radar",
                "data": [
                    {
                        "value": [13733, 5632, 7843, 30724, 29256, 15229, 46944, 60245, 17245, 40323, 40932, 7684, 8877, 5944, 8912, 16105, 4106, 27113, 45461, 742],
                        "name": "Hollman",
                    },
                    {
                        "value": [75455, 29622, 16263, 52188, 36423, 29931, 77388, 143401, 60180, 136024, 156055, 30938, 40725, 14242, 21539, 47474, 8407, 49404, 66658, 951],
                        "name": "Claudia",
                    },
                    {
                        "value": [105245, 33490, 12306, 41040, 32772, 25109, 61381, 121279, 55701, 113509, 162459, 31785, 33212, 15315, 18903, 43529, 6710, 40987, 54339, 608],
                        "name": "Galán",
                    },
                    {
                        "value": [45830, 15412, 5757, 15871, 13208, 9705, 26969, 47262, 20990, 47822, 68189, 14837, 13723, 6759, 9106, 17655, 2902, 16570, 23184, 152],
                        "name": "MiguelU",
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




st.write("""
**Credits**
- Software build by `Novus Vote` with `Registraduría General de la Nación` & `CentroDemocrático` data
""")
st.write('---')


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
