import numpy as np

A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])

C = np.sort(A,axis=1)
B = np.sort(A,axis=0)
print(C)
print(B)