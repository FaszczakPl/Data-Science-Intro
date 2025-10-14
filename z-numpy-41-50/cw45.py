import numpy as np

A = np.array([[[1, 2, 3],
               [6, 3, 2]]])

A = np.squeeze(A,axis=0)
print(A)