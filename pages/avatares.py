import streamlit as st
import graphviz
import random
import time

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


st.graphviz_chart(graph)


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["user"]):
        st.markdown(message["👋Bienvenido a esta Campaña Electoral: dime ¿cuál equipo deseas apoyar?"])
# React to user input
if prompt := st.chat_input("Dímelo de una"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Excelente, bienvenido ",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
