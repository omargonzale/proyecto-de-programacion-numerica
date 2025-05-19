import numpy as np

# Matriz de coeficientes
A = np.array([[4, -2, 1],[-2, 4, -2],[1, -2, 4]])
b = np.array([11, -16, 17])

print("Matriz de coeficientes 1:\n", A)
print("\nVector de terminios independientes: ", b)

C = np.linalg.solve(A, b)
print("\nSolucion por Gauss-Jordan: ",C)

def er(vr, vn):
    return abs((vr - vn) / vr) * 100

AI = np.linalg.inv(A)
print("\nMatriz Inversa\n",AI)

D= np.matmul(AI,b)
print("\nSolucion por Matriz Inversa: ",D)

Detg=np.linalg.det(A)
Detx=np.linalg.det(np.array([[11, -2, 1],[-16, 4, -2],[17, -2, 4]]))
Dety=np.linalg.det(np.array([[4, 11, 1],[-2, -16, -2],[1, 17, 4]]))
Detz=np.linalg.det(np.array([[4, -2, 11],[-2, 4, -16],[1, -2, 17]]))

x=Detx/Detg
y=Dety/Detg
z=Detz/Detg

print("\nSolucion por determinantes: x= ",x,"y= ",y, "z= ",z)

print("\nDescomposicion de LU")
L=np.zeros((3,3))
U=np.zeros((3,3))

L[0][0] = 1
L[1][1] = 1
L[2][2] = 1
U[0,:] = A[0,:]
L[1][0] = A[1][0]/U[0][0]
U[1][1] = A[1][1]-L[1][0]*U[0][1] 
U[1][2] = A[1][2]-L[1][0]*U[0][2] 
L[2][0] = A[2][0]/U[0][0] 
L[2][1] = (A[2][1]-L[2][0]*U[0][1])/U[1][1]
U[2][2] = A[2][2]-L[2][0]*U[0][2]-L[2][1]*U[1][2]
print(L)
print(U)

print("\nDescomposicion de Cholesky")

CH=np.zeros((3,3))
CH[0][0] = np.sqrt(A[0,0])
CH[1][0] = (A[1,0])/(CH[0,0])
CH[2][0] = (A[2,0])/(CH[0,0])
CH[1][1] = np.sqrt((A[1,1])-(CH[1,0]*CH[1,0]))
CH[2][1] = ((A[2,1])-(CH[1,0]*CH[2,0]))/(CH[1,1])
CH[2][2] = np.sqrt((A[2,2])-pow(CH[2,0],2)-pow(CH[2,1],2))

CHtrans= CH.T
print(CH)
print("\n",CHtrans)