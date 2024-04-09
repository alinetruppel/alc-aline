import numpy as np

A=np.array([[1 ,1,-1],[0,-1,3],[0,0,-1]]) # Exemplo da aula de matriz triangular superior
b=np.array([[2], [-4], [10]])             # Exemplo da aula de matriz b composta por 3 linhas x 1 coluna.  

def subst_regressiva(A: np.ndarray, b: np.ndarray) -> np.ndarray:

    n = len(A)                      # retorna o número de linhas da matriz A.
    x = np.zeros_like(b)            #Inicia um vetor x de zeros do tamanho de b.

    if len(b) != n:                 # verifica se o quantidade de linhas de b é igual a quantidade de linhas de A, caso contrário dá erro.
        raise ValueError ("O vetor coluna precisa ter a mesma quantidade de linhas da matriz triangular.")

    for k in range(n):              # verifica se a matriz é quadrada.
        if len(A[k]) != n:
            raise ValueError ("A matriz não é quadrada.")
        
    for v in range(n):              # verifica se a matriz é triangular superior.
        for u in range( v + 1, n):
            if A[u][v] != 0:
                raise ValueError ("A matriz não é triangular superior.")

    for k in range (n-1, -1, -1):   # Verifica se existe elemento nulo na diagonal da matriz triangular superior
        if A[k, k] == 0:
            raise Exception("Elemento não pode ser zero na diagonal da matriz triangular superior")
        
    x[n-1] = b[n-1]/A[n-1, n-1]     # Calcula a ultima linha da matriz triangular superior, primeira variável x, para poder inicializar o sistema.
    N = np.zeros((n,n))             # Inicia a variável N (numerador da fração no cálculo de x) como uma matriz de zeros.

    for i in range(n-2, -1, -1):
        s = 0                       # inicia a variável s (soma).
        for j in range (i+1, n):
            s += A[i, j]*x[j]       # Faz a soma acumulada s=s+aij*xj, sendo que o primeiro x já foi iniciado (linha 27).

        N[i, i] = b[i] - s          # Numerador da fração, para cáculo de x.
        x[i] = N[i, i]/A[i, i]      # Cálculo final de x.

    return x

x=subst_regressiva(A,b)             # Aplicando a função.
print(x)                            # Impressão do resultado.