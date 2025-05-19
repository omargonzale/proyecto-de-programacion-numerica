import numpy as np

g1 = lambda t: 2 * np.cos(2 * t)
g2 = lambda t: -t**2 - t/2 + 4
g3 = lambda t: np.exp(-t**2)

calcular_error = lambda valor_real, valor_calculado: round(abs((valor_real - valor_calculado) / valor_real) * 100, 4)

inicio = [0, 0.5, 0]
fin = [np.pi/4, 1.5, 1]
lista_funciones = [g1, g2, g3]
titulos = ['g1(t) = 2*cos(2t)', 'g2(t) = -t^2 - t/2 + 4', 'g3(t) = exp(-t^2)']
valores_reales = [1, 2.416666666, 0.7475]

def metodo_simpson_1_3(func, x0, xf):
    xm = (x0 + xf) / 2
    aproximacion = (xf - x0) * (func(x0) + 4 * func(xm) + func(xf)) / 6
    return round(aproximacion, 4)

def metodo_simpson_3_8(func, x0, xf):
    paso = (xf - x0) / 3
    aproximacion = (xf - x0) * (func(x0) + 3 * func(x0 + paso) + 3 * func(x0 + 2*paso) + func(xf)) / 8
    return round(aproximacion, 4)

for idx in range(len(lista_funciones)):
    funcion = lista_funciones[idx]
    x_inicial = inicio[idx]
    x_final = fin[idx]
    valor_analitico = valores_reales[idx]

    resultado_1_3 = metodo_simpson_1_3(funcion, x_inicial, x_final)
    resultado_3_8 = metodo_simpson_3_8(funcion, x_inicial, x_final)
    error_1_3 = calcular_error(valor_analitico, resultado_1_3)
    error_3_8 = calcular_error(valor_analitico, resultado_3_8)

    print(f'Función {idx + 1}:\n')
    print(f'  {titulos[idx]} en el intervalo [{round(x_inicial, 4)}, {round(x_final, 4)}]')
    print(f'    Simpson 1/3 ---> Resultado: {resultado_1_3} ---> Error relativo: {error_1_3}%')
    print(f'    Simpson 3/8 ---> Resultado: {resultado_3_8} ---> Error relativo: {error_3_8}%\n')