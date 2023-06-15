import streamlit as st
import graphviz

st.set_page_config(layout="wide", page_title="Novus Vote 🗳️ Tecnología Electoral", page_icon="🗳️")

st.title('Novus Vote 🗳️')
st.header("Guiones de Interacción de Avatares 🤖")

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('Bienvenida', 'Introducción')
graph.edge('Introducción', 'Identificación')
graph.edge('Identificación', 'Bienvenida')
graph.edge('Bienvenida', 'Entrenamiento')
graph.edge('Entrenamiento', 'Teoría')
graph.edge('Entrenamiento', 'Pruebas')
graph.edge('Entrenamiento', 'Reporte y Ranking TOTAL')
graph.edge('Pruebas', 'Examen')
graph.edge('Examen', 'DíaE')
graph.edge('DíaE', 'ReporteDíaE')
graph.edge('DíaE', 'Reporte y Ranking TOTAL')
graph.edge('ReporteDíaE', 'Reporte y Ranking TOTAL')
graph.edge('Pruebas', 'Reporte y Ranking TOTAL')

st.graphviz_chart(graph)
