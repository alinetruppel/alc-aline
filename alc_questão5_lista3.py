import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la
import math

# letra (a)======================================================================

def wilkinson_bidiagonal(n): # Função matriz wilkinson_bidiagonal
    b=np.ones(n-1)  
    B=np.diag(b*n, k=1) # fazendo uma matriz com a diagonal superior com todos os termos iguais a n.
   
    A=np.arange(1, n+1)
    A=sorted(A,reverse=True)
    A=np.diag(A) # fazendo uma matriz com diagonal principal em ordem decrescente, iniciando por n.

    R=A+B # A matriz resultante wilkinson_bidiagonal das matrizes criadas.
   
    return R



nn=10
C=wilkinson_bidiagonal(nn)
# D=np.linalg.cond(C)
print(C)
# print(D)


#letra(c)==============================================================

d=20
F=wilkinson_bidiagonal(d)
print(F)

eigenvalues, eigenvectors=la.eig(F) # Cálculo dos autovalores.
print(eigenvalues)
print(np.linalg.cond(F))


F[d-1,0]=(10**(-10)) # Fazendo o elemento F(20,1) da matriz ser 10^(-10).
eigenvalues1, eigenvectors1=la.eig(F) # Novo calculo dos autovalores.
print(eigenvalues1)
print(np.linalg.cond(F))


#letra(b)===============================================================
n=15
vetor_cond=[]
for n in range(1,n+1):
        C=np.linalg.cond(wilkinson_bidiagonal(n)) # Calcula o  numero de condicionamento.
        vetor_cond.append(C) # Salva em um vetor
        

# print(vetor_cond)
# print(len(vetor_cond))

X=np.arange(1, n+1)
plt.plot(X,vetor_cond)

# Adicionar rótulos aos eixos
plt.xlabel('Dimensão da Matriz')
plt.ylabel('Número de Condicionamento')

# Adicionar título ao gráfico
plt.title('Gráfico do Número de Condicionamento')

# Exibir o gráfico
plt.show()

#============================================================================================

















