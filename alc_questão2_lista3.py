import numpy as np
import math

u=np.array([[0], [2], [-2]]) 
v=np.array([[1], [1], [1]]) 

def crossprod(u: np.ndarray, v: np.ndarray) -> np.ndarray:

    u=np.array(u,dtype=float)
    v=np.array(v,dtype=float)

    Lin1,Col1 = u.shape
    Lin2,Col2 = v.shape

    # Entrada com o vetor u 3 x 1.  
    if Lin1!=3 or Col1!=1:
        raise ValueError ("O vetor precisa ter 3 linhas e 1 coluna")
    
    # Entrada com o vetor v 3 x 1.  
    if Lin2!=3 or Col2!=1:
        raise ValueError ("O vetor precisa ter 3 linhas e 1 coluna")
        
    z = np.zeros_like(u) 

    z[0,0]=(u[1,0]*v[2,0]) - (v[1,0]*u[2,0])
    z[1,0]=(u[2,0]*v[0,0]) - (v[2,0]*u[0,0])
    z[2,0]=(u[0,0]*v[1,0]) - (v[0,0]*u[1,0])

    return z # Saída será um vetor (3x1), onde z=u x v
 
A=crossprod(u,v) # A função foi feita para um vetor coluna.
#A1=np.cross(u.T,v.T) # Para o produto vetorial do numpy o vetor precisa ser linha. Checar resultado.
print(A)
#print(A1.T)

B=crossprod(v,u) # A função foi feita para um vetor coluna.
#B1=np.cross(v.T,u.T) # Para o produto vetorial do numpy o vetor precisa ser linha. Checar resultado.
print(B)
#print(B1.T)

C=np.inner(A.T, u.T) # Numpy usa vetor linha, logo foi necessário fazer a transposta.
print(C)

D=np.inner(B.T, v.T) # Numpy usa vetor linha, logo foi necessário fazer a transposta.
print(D)

