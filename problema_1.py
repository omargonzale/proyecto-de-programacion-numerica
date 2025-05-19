"""
tarea 1 
Omar Eduviges Gonzalez Ochoa
374165
"""

def pedir_numero():
    try:
        N = int(input("Por favor, ingrese un número entero y positivo: "))
        if N <= 0:
            print("Error: El número debe ser positivo.")
        else:
            print(f"El número ingresado es: {N}")
    except ValueError:
        print("Error: No has ingresado un número entero válido.")


pedir_numero()