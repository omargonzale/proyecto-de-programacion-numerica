import numpy as np 
import matplotlib.pyplot as plt
f=lambda x:8*x*np.sin(x)*np.exp(-x)-1
xo=-0.3
xni=0.5
n=5 
error_rel=lambda vn , va:(abs((va-vn)/vn)*100)
 
for i in range (n):
     x_nueva= xo-(f(xo)*(xni-xo)/(f(xni)-f(xo)))
     er=round(error_rel(x_nueva,xo),4)
     print('..........................................')
     print(f'i={i+1} | x_i={x_nueva} | er={er}')
     
     xni=xo
     xo=x_nueva
     
x=np.linspace(-5,5,100)
plt.plot(x,f(x))
plt.plot(xo,f(xo),'ro')
plt.grid()
plt.show()

 