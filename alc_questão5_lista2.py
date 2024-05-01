import numpy as np
from numpy import linalg as LA

# Exercicio 6.38
P1= np.array([[-0.4082, 0.43644, 0.80178] , [-0.8165, 0.21822, -0.53452], [-0.40825, -0.87287, 0.26726]])

P2= np.array([[-0.51450, 0.48507, 0.70711] , [-0.68599, -0.72761, 0.00002], [0.51450, -0.48507, 0.70711]])

# Exercicio 6.39

P3= np.array([[-0.58835, 0.70206, 0.40119] , [-0.78446, -0.37524, -0.49377], [-0.19612, -0.60523, 0.77152]])

P4= np.array([[-0.47624, -0.4264, 0.30151] , [0.087932, 0.86603, -0.40825], [-0.87491, -0.26112, 0.86164]])

def orthogonal_definition(A: np.ndarray):
    n = len(A)  
    y=np.eye(n)

    x=A.T @ A 
    x=np.round(x)
    
    return print(np.array_equal(x,y)) # por definição para ser ortogonal A.T@A é igual a matriz identidade.
    
def orthogonal_vectors(A: np.ndarray):

    n = len(A)  
    x = np.zeros_like(A)

    for i in range(n):              
        for j in range( i + 1,n):
            x[i,j]=A[:,i].T@A[:,j] 
            x[j,i]=x[i,j]
            x=np.round(x)
            if x[i,j]==0: T1=1 # se ortogonal x[i,j]=x[j,i] igual a 0  ( apenas para i diferente de j), Teste 1 é atendido (T1=1)
            else: T1=0    
                   

    for n in range(n-1,-1,-1):
        #x[n,n]= A[:,n].T@A[:,n]      
        x[n,n]=LA.norm(A[:,n]) 
        x=np.round(x)
        if x[n,n]==1: T2=1 # se ortogonal x[n,n] tem coluna de tamanho (norma) igual a 1, Teste 2 é atendido (T2=1)
        else: T2=0

 
    if T1==1 and T2==1: # Se ambos os testes foram atendidos é ortogonal caso contrário não será.
        return print(bool(1))
    else:
        return print(bool(0))

    
 
R1=orthogonal_definition(P1)
R2=orthogonal_definition(P2)
R3=orthogonal_definition(P3)
R4=orthogonal_definition(P4)

R11=orthogonal_vectors(P1)
R22=orthogonal_vectors(P2)
R33=orthogonal_vectors(P3)
R44=orthogonal_vectors(P4)