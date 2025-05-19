#birge-vieta
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1*x**3 - 5*x**2 + 5*x - 1  


a = np.array([1, -5, 5, -1])
xcero = 0.8  
b = np.empty(len(a))
c = np.empty(len(a))

iteraciones = 10
n = len(a)

for i in range(1, iteraciones + 1):
    for j in range(n):
        if j == 0:
            b[j] = a[j]
            c[j] = a[j]
        else:
            b[j] = a[j] + xcero * b[j - 1]
            c[j] = b[j] + xcero * c[j - 1]

    xcero_viejo = xcero  
    xcero = xcero - (b[n - 1] / c[n - 2])  

    print(f'\n Iteración: {i}')
    print(f'xi = {xcero_viejo}')
    print('b:', b)
    print('c:', c)


x = np.linspace(-1, 3, 100)  
plt.plot(x, f(x), label="f(x)")
plt.plot(xcero, f(xcero), 'ro', label="Raíz encontrada")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(xcero, color='red', linestyle='dashed', linewidth=0.5)
plt.grid()
plt.legend()
plt.show()