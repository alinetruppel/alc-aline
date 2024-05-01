import numpy as np
from random import random
from numpy.linalg import matrix_rank
from numpy import linalg as LA

u1=np.random.rand(5,1)
v1=np.random.rand(5,1)
t1=u1@(v1.T) #v1.T => Fazer o transposto.
r1=matrix_rank(t1)  # denota o numero de linhas ou colunas linearmente independentes da matriz.
print(r1)

nu1=LA.norm(u1, 2)
nv1=LA.norm(v1, 2)
nr1=nu1*nv1
print(nr1)

n1=LA.norm(t1,2)
print(n1)

eigenvalues1, eigenvectors1=LA.eig(t1.T @ t1)
E1=np.sqrt(max(eigenvalues1))
print(E1)

#---------------------------------------------
u2=np.random.rand(15,1)
v2=np.random.rand(15,1)
t2=u2@(v2.T)
r2=matrix_rank(t2)
print(r2)

nu2=LA.norm(u2, 2)
nv2=LA.norm(v2, 2)
nr2=nu2*nv2
print(nr2)

n2=LA.norm(t2,2)
print(n2)

eigenvalues2, eigenvectors2=LA.eig(t2.T @ t2)
E2=np.sqrt(max(eigenvalues2))
print(E2)

#---------------------------------------------
u3=np.random.rand(25,1)
v3=np.random.rand(25,1)
t3=u3@(v3.T)

r3=matrix_rank(t3) 
print(r3)

nu3=LA.norm(u3, 2)
nv3=LA.norm(v3, 2)
nr3=nu3*nv3
print(nr3)

n3=LA.norm(t3,2)
print(n3)

eigenvalues3, eigenvectors3=LA.eig(t3.T @ t3)
E3=np.sqrt(max(eigenvalues3))
print(E3)

#---------------------------------------------

