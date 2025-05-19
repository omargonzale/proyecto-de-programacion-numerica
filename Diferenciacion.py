#Omar Eduviges Gonzalez Ochoa 
from scipy.misc import derivative

g = lambda t: -t**2 - t/2 + 4
pasos = [0.2, 0.1]
punto = 0

def metodo_adelante(func, x, h):
    f1 = func(x + h)
    f2 = func(x + 2*h)
    return round((-f2 + 4*f1 - 3*func(x)) / (2*h), 4)

def metodo_atras(func, x, h):
    b1 = func(x - h)
    b2 = func(x - 2*h)
    return round((3*func(x) - 4*b1 + b2) / (2*h), 4)

def metodo_centrada(func, x, h):
    c1 = func(x + h)
    c2 = func(x + 2*h)
    c3 = func(x - h)
    c4 = func(x - 2*h)
    return round((-c2 + 8*c1 - 8*c3 + c4) / (12*h), 4)

print('========== Derivadas Analíticas ==========')
print()
for paso in pasos:
    valor_analitico = derivative(g, punto, paso)
    print(f'Para h = {paso} ----> Derivada analítica: {round(valor_analitico, 4)}')
print()

print('========== Derivadas Numéricas ==========')
print()
for paso in pasos:
    adelante = metodo_adelante(g, punto, paso)
    atras = metodo_atras(g, punto, paso)
    centrada = metodo_centrada(g, punto, paso)
    
    print(f'Para h = {paso}:')
    print(f'  Derivada hacia adelante: {adelante}')
    print(f'  Derivada hacia atrás:    {atras}')
    print(f'  Derivada centrada:        {centrada}')
    print()