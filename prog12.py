#Escriba una función que haga la factorización QR de una matriz cuadrada
#arbitraria; puede usar numpy.

import numpy as np

def qr_factorization(matrix):
    
    n = matrix.shape[0]  
    Q = np.zeros((n, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = matrix[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], matrix[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R

#Acontinuación se muestra un ejemplo

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

Q, R = qr_factorization(A)

print("Q:")
print(Q)
print("\nR:")
print(R)








