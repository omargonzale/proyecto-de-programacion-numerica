##metodo regla falsa 
import matplotlib.pyplot as plt
import numpy as np 

f=  lambda x: (2*x*np.cos(2*x))-(x+1)**2
error_rel=lambda vn , va:(abs((va-vn)/vn)*100)
xr=-2.1913
a=-3
b=-2
xi=round((a+b)/2,4)
num_iteraciones=5

for i in range (num_iteraciones):
    aviejo=a
    bviejo=b
    xi=b-((f(b)*(a-b))/(f(a)-f(b)))
    fa=f(a)
    fxi=f(xi)
    er=round(error_rel(xr,xi),4)
    
    if fa*fxi< 0:
       b=xi
      
    else:
      a=xi
        
    print('.......................................................')
    print(f'i={i+1} | a={aviejo} | b={bviejo} | xi={xi} | er={er}%')  
    
     
x=np.linspace(-5,5,100)
plt.plot(x,f(x))
plt.plot(xi,f(xi),'ro')
plt.grid()
plt.show()