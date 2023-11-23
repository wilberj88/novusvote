import streamlit as st
import streamlit.components.v1 as com
com.html("""
<div>
<style>
h1.heading{
     background-color:blueviolet;
     color:lightyellow;
     border-radius:30px;
     text-align:center;
}
h1 {
  text-align: center;
  margin: 35px 0 20px 0 !important;
}
</style>
<h1 class="heading">
Conctáctanos
</h1>
<form action="https://formsubmit.co/fb63e36d2da2ed5e485b96aa352037f6" method="POST">
     <h1 class="heading">Name</h1>
     <input type="text" name="name" required>
     <h1 class="heading">Email</h1>
     <input type="email" name="email" required>
     <h1 class="heading">Mensaje</h1>
     <textarea placeholder="Escribe tu mensaje aquí" name="message" required></textarea>
     <h1 class="heading">Enviar</h1>
     <button type="submit">Send</button>
</form>
</div>
""", height=600, scrolling=True)
