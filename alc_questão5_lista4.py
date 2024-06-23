import numpy as np
import scipy
import scipy.linalg

def Modqrgrsch(A: np.ndarray) -> np.ndarray:
    m,n = A.shape
    Q = np.zeros((m, n), dtype=float)
    R = np.zeros((n, n), dtype=float)
  
    for i in range(n):
        Q [:, i] = A [:, i]
        for j in range(i):
            R[j, i] = np.dot(Q[:, j].T, Q[:, i])
            Q[:, i] -= np.dot(R[j, i], Q[:, j])
        R[i, i]=np.linalg.norm(Q[:, i])
        Q[:, i] /= R[i, i]

    return Q, R

A = np.array([ [1.0, 9, 0, 5, 3, 2], [-6.0, 3, 8, 2, -8, 0], [3.0, 15, 23, 2, 1,7], [3, 57, 35, 1, 7, 9], [3, 5, 6, 15, 55, 2], [33, 7, 5, 3, 5, 7] ])
print(A)

Q, R=Modqrgrsch(A)
Q=np.round(Q,4)
R=np.round(R,4)
print(Q)
print(R)

M = np.dot(Q,R)
M=np.round(M,4)
print(M)

Q1, R1 = np.linalg.qr(A,mode='complete')
Q1=np.round(Q1,4)
R1=np.round(R1,4)
print(Q1)
print(R1)

M1=np.dot(Q1,R1)
M1=np.round(M1,4)
print(M1)