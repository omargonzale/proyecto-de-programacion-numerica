"""
Tarea 4 
Omar Eduviges Gonzalez Ochoa
374165
"""
import numpy as np
import random

N=4
x=[random.randint(1,9)for _ in range(N)]

matriz=[]
for i in range(1,N+1):
   fila=[]
   for j in range(N):
       fila.append(x[j]*i)
   matriz.append(fila)
for fila in matriz:
    
    print(fila)     
