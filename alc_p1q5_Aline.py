import numpy as np

#A=np.array([[5.0, 3],[3,2]])
#A=np.array([[3.0, 2, 8],[2, 4, 6],[1, 1, 4]])
A=np.array([[1, 2, 4],[1, 2, 9],[3, 5, 3]])

def inversa_eliminacao(matriz: np.ndarray)-> np.ndarray:
    matriz=np.array(matriz,dtype=float)
    n = len(matriz) 
    
    inversa = np.eye(n)  # Criar a matriz identidade

    for k in range (n-1, -1, -1):   # Verifica se existe elemento nulo na diagonal da matriz 
        if int(matriz[k, k]) == 0:
            raise Exception("Elemento não pode ser zero na diagonal da matriz")

   
    for i in range(n):
        # Normalizar a diagonal
        divisor = matriz[i,i]
        if divisor == 0:   # se o divirsor é zero, troca a linha.
            for k in range(i+1,n):
                if matriz[k][i]!=0: 
                    matriz[[i,k]]=matriz[[k,i]]
                    inversa[[i,k]]=inversa[[k,i]]
                    divisor=matriz[i][i]
                    
                    break
            else:            
                raise Exception(" Não pode ser zero")
        matriz[i,:]=matriz[i,:]/divisor
        inversa[i,:]=inversa[i,:]/divisor
               
        # Zero as outras linhas na coluna atual
        for j in range(n):
            if i != j:
                factor = matriz[j][i]                
                matriz[j,:]=matriz[j,:]-(factor * matriz[i,:])
                inversa[j,:]=inversa[j,:]-(factor * inversa[i,:])
                
    return inversa

A=inversa_eliminacao(A)
print(A)


#matriz=np.array([[5, 3],[3,2]])
#matriz=np.array([[3, 2, 8],[2, 4, 6],[1, 1, 4]])
#matriz=np.array([[1.0, 7, 9],[3, 5, 3],[4, 9, 2]])
#matriz=np.array([[3.0, 2, 8],[2, 4, 6],[1, 1, 4]])
matriz=np.array([[1.0, 2, 4],[1, 2, 9],[3, 5, 3]])
C=np.linalg.inv(matriz)
print(C)