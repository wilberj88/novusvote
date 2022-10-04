import streamlit as st

st.title('Hola, soy el Atento 🤖 de tu Mando que te ayudará a monitorizar y conseguir empleo')
a = st.text_input('¿En qué quieres trabajar?')

b = st.text_input('¿Cuánto deseas ganar como mínimo al mes?')

c = st.text_input('¿En cuál horario de trabajo te quedaría mejor?')

if a and b and c:
  st.write('Estamos preparando un Mando con el análisis de los empleos disponibles como <<',a, '>>, que permitan ganar <<', b, '>> en el horario que te cuadra de <<', c, '>>')
