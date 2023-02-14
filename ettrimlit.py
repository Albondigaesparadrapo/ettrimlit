import streamlit as st

mensaje = "Para colorear, :red[poner el texto entre corchetes] y delante el nombe del color con :"
st.markdown(mensaje)

st.success("Acsión exitosa :3")
st.info("Esto es solo para informar. Qué inútil")
st.warning("CUIDADO")
st.error("Yo te avise")

st.camera_input("sí.")
st.warning("Tu cara sí que es un error.")
