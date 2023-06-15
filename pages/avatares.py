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
graph.edge('Entrenamiento', 'zombie')
graph.edge('Entrenamiento', 'sleep')
graph.edge('Entrenamiento', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)
