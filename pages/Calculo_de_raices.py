import streamlit as st
import methods.rootCalculation as rC
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

st.markdown("<h1 style='text-align: center'>Calculo de raices</h1>'>", unsafe_allow_html=True)
st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

# Ingresar los límites
with col1:
    xl = st.number_input("Límite Inferior", -10.0, 10.0, 0.2, 0.1)

with col2:
    xu = st.number_input("Límite Superior", -10.0, 10.0, 1.7, 0.1)

with col3:
    var = st.text_input("Variable", "x")

with col4:
    tol = st.number_input("Tolerancia", value=0.5)

# Ingresar la función
with col5:
    func = st.text_input("Función", "x**3 - x")

st.divider()
# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)
st.sidebar.markdown('<hr style="margin: 5px 0px 0px 0px;"><h1>Métodos</h1>', unsafe_allow_html=True)
button_biseccion = st.sidebar.button('Método de la Bisección')
button_false_pos = st.sidebar.button('Método de la Falsa Posición')
button_newton = st.sidebar.button('Método de Newton-raphson')
button_secante = st.sidebar.button('Método de Secante')
button_variante = st.sidebar.button('Método Variante Secante')
button_punto_fijo = st.sidebar.button('Método Punto Fijo')

# with st.expander("Método de la Bisección"):
# # st.markdown("<h2>Método de la Bisección</h2>", unsafe_allow_html=True)
#     exec = st.button('Ejecutar')
if button_biseccion:
    st.markdown("<h2>Método de la Bisección</h2>", unsafe_allow_html=True)
    st.write(rC.bisectionMethod(func, xl, xu, tol,start_range,end_range, var))