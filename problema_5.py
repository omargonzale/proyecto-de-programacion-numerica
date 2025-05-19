"""
Tarea 5
Omar Eduviges Gonzalez Ochoa
374165
"""

import random

def generar_vector(N):
    return [random.randint(1, 9) for _ in range(N)]

def generar_matriz_filas(X, N):
    matriz = []
    for i in range(N): 
        fila = [X[i] * (j + 1) for j in range(N)]  # Corregido el índice para obtener los múltiplos correctamente
        matriz.append(fila)
    return matriz

def generar_matriz_columnas(X, N):
    matriz = []
    for i in range(N):
        fila = [X[j] * (i + 1) for j in range(N)]  # Corregido la lógica para que las columnas se llenen adecuadamente
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Valor de N
N = 5

# Generar vector
X = generar_vector(N)
print(f"Vector: {X}")

# Generar y mostrar matriz con múltiplos en las filas
matriz1 = generar_matriz_filas(X, N)
print("Matriz con múltiplos en las filas:")
imprimir_matriz(matriz1)

# Generar y mostrar matriz con múltiplos en las columnas
matriz2 = generar_matriz_columnas(X, N)
print("Matriz con múltiplos en las columnas:")
imprimir_matriz(matriz2)