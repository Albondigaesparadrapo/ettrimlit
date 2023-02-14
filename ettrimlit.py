import streamlit as st

mensaje = "Para colorear, :red[poner el texto entre corchetes] y delante el nombe del color con :"
st.markdown(mensaje)

st.success("Acsión exitosa :3")
st.info("Esto es solo para informar. Qué inútil")
st.warning("CUIDADO")
st.error("Yo te avise")

num1 = st.number_input("First number")
num2 = st.number_input("Second number")

signos = ("+","-","*","/")
resultado = st.radio("Signos",signos)

st.write(num1,resultado,num2,"=")

if resultado=="+":
	st.write(num1+num2)
if resultado=="-":
	st.write(num1-num2)
if resultado=="*":
	st.write(int(num1*num2)
if resultado=="/":
	if num2 != 0:
		st.write(num1/num2)
	elif num2 == 0:
		st.write("No puedes dividir entre 0.")
