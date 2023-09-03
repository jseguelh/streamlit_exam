# Importando las bibliotecas necesarias
import streamlit as st

# Título del Dashboard
st.title('Mi Primer Dashboard con Streamlit')

# Una entrada de texto
texto = st.text_input('Escribe algo aquí:')

# Mostrar el texto ingresado
st.write('Texto ingresado:', texto)

# Una entrada numérica
numero = st.slider('Elige un número:', min_value=0, max_value=100, value=50)

# Mostrar el número seleccionado
st.write('Número seleccionado:', numero)

# Un gráfico simple
import numpy as np
import matplotlib.pyplot as plt

# Generar datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear un gráfico
plt.figure(figsize=(8,4))
plt.plot(x, y, label=f'Seno de x multiplicado por {numero}', color = 'red')
plt.title('Gráfico de Seno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(plt)

# Botón de acción
if st.button('Presiona aquí!'):
    st.write('¡Botón presionado!')

# Ejecuta el dashboard ejecutando este script y visitando la URL que se muestra en la consola.
