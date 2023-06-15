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
graph.edge('Entrenamiento', 'runmem')
graph.edge('Pruebas', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('Pruebas', 'runmem')

st.graphviz_chart(graph)
