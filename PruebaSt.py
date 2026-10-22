import streamlit as st

st.title ("HOLA SOY JOHN FALLOUT")
st.write ("Quien eres tu?")
nombre = st.text_input("Pon tu nombre aca")

if st.button ("Si"):
    st.success (f"Hola {nombre}, necesito 3000$ para salvar a fallout city ahora mismo, si no lo haces, fallout city sera destruida por completo y no habra vuelta atras. Asi que por favor, ayudame a salvar a fallout city")

if st.button ("No"):
    st.error (f"Hola {nombre}, si no me ayudas a salvar a fallout city, fallout city sera destruida por completo y no habra vuelta atras. Asi que por favor, ayudame a salvar a fallout city")