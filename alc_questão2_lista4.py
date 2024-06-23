import numpy as np
import scipy
import scipy.linalg

 
def ludecomp(A: np.ndarray) -> np.ndarray:

    A=np.array(A,dtype=float)
    m,n = A.shape # calcula quantidade de Linhas (m) e colunas(n) de A
  
    if m != n: # Verifica se A é uma matriz quadrada m=n, se for diferente dá erro.
        raise ValueError ("Matriz tem que ser quadrada")
    
    L=np.eye(n,dtype=float) # Inicia L com a matriz identidade.
    P=np.eye(n,dtype=float) # Inicia L com a matriz identidade.
    U=np.zeros_like(A,dtype=float) # Computa matriz um com zeros, do tamanho de A
    int=0
    
    # Fazer a Eliminação de Gauss para obter L, U, e P
    for i in range(n):
        
        # Acha a Linha K dos valores máximos (Pivot)
        k = np.argmax(abs(A[i:n, i]))	
        pivot = i + k

         # Coforme o Livro Ford exemplo 11.12 comando abaixo necessário para resolver qq matriz ainda que singular
        if np.max(np.abs(A[pivot, i])) <= 1e-9:
            break

        
        if pivot!= i: # Fazendo as trocas de linhas
                A[[i, pivot], i:n] = A[[pivot, i], i:n]
                P[[i, pivot], :] = P[[pivot, i], :]
                L[[i, pivot], :i] = L[[pivot, i], :i]
                int = int + 1

        if A[i,i]!=0:      
            multip= A[i+1:n,i]/A[i,i] # Calcula os Multiplicadores.
            L[i+1:n,i]=multip # Preenche a Matriz L com os multiplicadores.
       
        for x in range(i+1, n): # faz as operações na matriz A
           for y in range(i+1, n):
               A[y, x] = A[y, x] - L[y, i] * A[i, x]

        A[i+1:n,i] = 0     # completa a matriz com zeros.
         
   
    U=A # U será a matriz final após modificação de A 

    return P, L, U     

#exemplos para testar
#A = np.array([[1, 4 , 7], [2, 5, 8], [3, 6, 9]], dtype=float) #singular
#A = np.array([ [7, 3, -1, 2.0], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
#A = np.array([[1, -3, 5.0], [2, -4, 7], [-1, -2, 1]])
#A = np.array([[3, 8, 1.0], [5, 2, 0], [6, 1, 12]])
#A = np.array([[1, 2 , 3], [2, 5, 4], [3, 5, 4]], dtype=float)
# Exemplo 11.12 do Ford
#A = np.array([ [-1, -1, 0, 1], [-1, 1, 1, 0], [1, 1, 1, 1], [2, 0, 1, 0] ])
A = np.array([[2, 1 , 3, 5], [1, 6, -1, 2], [3, 7, 2, 7], [5, 19, 0, 11]], dtype=float) #singular

print(A)

P, L, U =ludecomp(A)
print(P)
print(L)
print(U)

P1, L1, U1 = scipy.linalg.lu(A)
#Existe uma leve diferença do Algorithmo do Ford.
# Na implementação do scipy.linalg.lu, o resultado de P é transposto.
print(P1.T)
print(L1)
print(U1)