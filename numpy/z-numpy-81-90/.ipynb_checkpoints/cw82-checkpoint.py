import numpy as np

A = np.array(['001', '002', '003'])
B = np.array(['XC', 'YC', 'ZC'])
C = np.char.add(A,B)
print(C)