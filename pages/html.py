import streamlit as st
import streamlit.components.v1 as com
com.html("""
<div>
<h1>
Conctáctanos
</h1>
<form action="https://formsubmit.co/wilber.jimenez.hdz@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
</div>
""")
