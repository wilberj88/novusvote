import streamlit as st
import streamlit.components.v1 as com
com.html("""
<div>
<style>
h1.heading{
     background-color:blueviolet;
     color:lightyellow;
     border-radius:20px;
     text-align:center;
}
</style>
<h1 class="heading">
Conctáctanos
</h1>
<form action="https://formsubmit.co/wilber.jimenez.hdz@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
</div>
""")
