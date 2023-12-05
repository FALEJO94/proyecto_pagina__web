import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
from math import e

def calculate_y(x_values, expression):
  return [expression.subs({x: xi}) for xi in x_values]

def bisectionMethod(func, xl, xu, tol, start_range, end_range, var):
  # Tolerancia y valores iniciales
  global x
  xr = None
  xr_ant = xu
  error = tol + 1
  it = 1
  x = sp.symbols(var)
  y = sp.sympify(func)

  # Dataframe para almacenar los resultados
  columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
  tabla = pd.DataFrame(columns=columnas)

  # Espacio reservado para la figura
  fig_placeholder = st.empty()
  tablita = st.empty()
  fig_placeholder.markdown(
    """
    <style>
    div[data-testid="stBlock"] {
        width: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
  while error > tol:
    # Evaluamos la función en los puntos del intervalo
    fxl = y.subs({x: xl}).evalf()
    fxu = y.subs({x: xu}).evalf()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.set_title(f"${sp.latex(y)}$")
    ax.grid()

    # Límites xl y xu
    ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
    ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    # Calculamos la raíz
    xr = round((xl + xu) / 2, 4)
    fxr = y.subs({x: xr}).evalf()

    # Pintamos el punto intermedio
    ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
    ax.legend()

    # Actualizamos el error y la tabla
    error = np.abs((xr - xr_ant) / xr) * 100 if xr != 0 else 0
    nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)': fxr}
    tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)
    # Actualizamos los límites
    if fxl * fxr < 0:
        xu = xr
    elif fxl * fxr > 0:
        xl = xr
    elif fxl * fxr == 0:
        st.success(f"La raíz está en: ({round(xr,4)}, {round(fxr,4)})")
        break

    xr_ant = xr
    it += 1

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

class RootCalculation:
    def __init__(self):
        print("Esto es el init")
        
        

def falceMethod(func, xl, xu, tol, start_range, end_range, var):
  
  y = sp.sympify(y)
  f = sp.lambdify(x, y)
  #tol = float(input("Ingrese el valor de la tolerancia: "))
  er = tol + 1
  xrant = xl

  columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
  tabla = pd.DataFrame(columns=columnas)

  plt.figure()
  fig, ax = plt.subplots()

  #r = np.linspace (xl-0.5,xu+0.5, 100)
  r = np.linspace(min(xl, xu) - 2, max(xl, xu) + 2, 100)

  ax.plot(r,f(r),color='blue')#, label="$X^3 - X$")
  #plano cartesiano (EJES)
  ax.vlines(x=0,ymin=round(min(f(r)),4)-0.5,ymax=round(max(f(r)),4)+0.5,color='k')
  ax.hlines(y=0,xmin=round(min(r),4)-0.5,xmax=round(max(r),4)+0.5,color='k')
 
  #ax.set_title('${X^3-X}$')
  #ax.plot(r, fx, color='blue', label="$(667.38 / x) * (1 - e^{-0.146843 * x}) - 40$")
  ax.set_title('${}$'.format(sp.latex(y)))
  #ax.set_title('${}$'.format(sp.latex(y)).replace('e', 'e^{\\text{Euler}}'))
  ax.grid()

  #limites xl y xu
  ax.vlines(x=xl, ymin=0, ymax=f(xl), color='k', linestyle='--', label=f'$x_l=${xl}')
  ax.vlines(x=xu, ymin=0, ymax=f(xu), color='k', linestyle='--', label=f'$x_u=${xu}')
  #xr=un número
  xr=1

  while er > tol:

    nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': er, 'f(Xl)': f(xl), 'f(Xu)': f(xu), 'f(Xr)': f(xr)}
    nueva_fila = pd.DataFrame([nueva_fila])
    tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

    xr = round(((f(xl) * xu) - (f(xu) * xl)) / (f(xl) - f(xu)), 4)

    ax.plot(xr,f(xr),color='red',label=f'$Raiz=${xr}',marker='o')
    ax.legend()

    #plt.show()

    if (f(xl) * f(xr)) < 0:
      xu = xr
    elif (f(xl) * f(xr)) > 0:
      xl = xr
    elif (f(xl) * f(xr)) == 0:
      print("termine")
    er = abs((xr - xrant) / xr) * 100
    xrant = xr
  tabla
  class RootCalculation:
    def __init__(self):
        print("Esto es el init")