import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote - Diego Molano Aponte", page_icon="🗳️")

st.title('Novus Vote 🗳️ - Diego Molano')
st.header("Centrales de Mando para la Operación Política y Electoral")
st.write("Focaliza el monitoreo de todos tus frentes")

etapa = st.selectbox("Etapa Electoral",
        ("Pre Campaña", "Campaña", "Día Electoral", "Post Campaña"))

if etapa is "Pre Campaña":
        st.write("Requieres los monitores de: Firma + Votos...")










st.button('Calcular diagnóstico gratuito'):
    st.header("Requerimientos de Campaña")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Inversión", "70 M USD", "7.2 M USD")
    col2.metric("Líderes", "9 mpl", "-8%")
    col3.metric("Sentimiento", "86%", "4%")
    col4.metric("Votos", "50K mpl", "4K")
    st.write("Desagregación de votos por barrios de acuerdo con las votaciones históricas")
    #datos
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
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
    st.write("Líderes necesarios para votación mínima")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)
    st.write("Financiación necesaria")
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

    st.header("Requerimientos de Candidato")
    chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])
    st.bar_chart(chart_data)

    df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.altair_chart(c, use_container_width=True)

# Data src:  https://www.kaggle.com/manohar676/hotel-reviews-segmentation-recommended-system
# Credit to: Manohar Reddy
    df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Plotly_Graphs/Radar-chart/ExistingHotels_CustomerVisitsdata-1554810038262.csv")
    df = df[df['Hotelid'].isin(['hotel_101','hotel_102','hotel_103'])]
    print(df.iloc[:20, :8])

    df = df.groupby('Hotelid')[['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                    'Rooms_rating','Checkin_rating',
                                    'Businessservice_rating']].mean().reset_index()
    print(df)

# Convert from wide data to long data to plot radar chart
    df = pd.melt(df, id_vars=['Hotelid'], var_name='category', value_name='rating',
                     value_vars=['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                 'Rooms_rating','Checkin_rating','Businessservice_rating'],
        )
    print(df)

# radar chart Plotly examples - https://plotly.com/python/radar-chart/
# radar chart Plotly docs = https://plotly.com/python-api-reference/generated/plotly.express.line_polar.html#plotly.express.line_polar
    fig = px.line_polar(df, r='rating', theta='category', color='Hotelid', line_close=True,
                                    line_shape='linear',  # or spline
                            hover_name='Hotelid',
                            hover_data={'Hotelid':False},
                            markers=True,
                            # labels={'rating':'stars'},
                            # text='Hotelid',
                            # range_r=[0,10],
                            direction='clockwise',  # or counterclockwise
                            start_angle=45
                            )
        # fig.update_traces(fill='toself')
    fig.show()



st.write("""
**Credits**
- Software build by `Novus Wilber` with `Registraduría General de la Nación` data
""")
st.write('---')


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
