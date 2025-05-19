"""
Tarea 6 
Omar Eduviges Gonzalez Ochoa
374165
"""
import numpy as np
import matplotlib.pyplot as plt

# Definir los valores de x
x = np.linspace(-2, 2, 100)

# Definir las tres funciones
y1 = x
y2 = x ** 2
y3 = x ** 3

# Crear una figura y una malla de subgráficas (3 filas, 1 columna)
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Gráfica para y = x
axs[0].plot(x, y1, color='blue', linestyle='--', label='y=x')
axs[0].set_title('Gráfica de y = x')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].grid(True)
axs[0].legend()

# Gráfica para y = x^2
axs[1].plot(x, y2, color='green', linestyle='-.', label='y=x^2')
axs[1].set_title('Gráfica de y = x^2')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].grid(True)
axs[1].legend()

# Gráfica para y = x^3
axs[2].plot(x, y3, color='red', linestyle=':', label='y=x^3')
axs[2].set_title('Gráfica de y = x^3')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].grid(True)
axs[2].legend()

# Ajustar el espaciado entre las subgráficas
plt.tight_layout()

# Mostrar la gráfica
plt.show()