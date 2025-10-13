import numpy as np

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])

#moje tez dobre
n = len(A)
for i in range(n):
    print(np.any(A[i]==B[i]))

#proste
print(A==B)