import numpy as np
import matplotlib.pyplot as plt
xo=0.3
f=lambda x:8*x*np.sin(x)*np.exp(-x)-1
f_deriv=lambda x: (8*np.exp(-x))*(np.sin(x)+x*np.cos(x)-x*np.sin(x))
error_rel=lambda vn , va:(abs((va-vn)/vn)*100)
n=5

for i in range(n):
   
   x_nueva= xo-(f(xo)/f_deriv(xo))
    
   er=round(error_rel(x_nueva,xo),4)
   print('.........................................')
   print(f'i={i+1} | xi={x_nueva} | er={er}')
   xo=x_nueva

x=np.linspace(-5,5,100)
plt.plot(x,f(x))
plt.plot(x,f_deriv(x))
plt.plot(xo,f(xo),'ro')
plt.plot(xo,f_deriv(xo),'ro')
plt.grid()
plt.show()

