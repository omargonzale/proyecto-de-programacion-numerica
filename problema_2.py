""""
Tarea 2 
Omar Eduviges Gonzalez Ochoa 
374165
"""
import random

def pedir_numero():
    try:
        # Pedimos al usuario un número entero
        N = 4
        
        # Verificamos si el número es positivo
        if N <= 0:
            print("Error: El número debe ser positivo.")
        else:
            # Generamos un vector de N valores aleatorios entre 1 y 9
            vector = [random.randint(1, 9) for _ in range(N)]
            print(f"El vector generado con {N} valores aleatorios entre 1 y 9 es: {vector}")
    
    except ValueError:
        print("Error: No has ingresado un número entero válido.")

# Llamada a la función para pedir el número y generar el vector
pedir_numero()