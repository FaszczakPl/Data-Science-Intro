import numpy as np

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
 
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
 
C = np.array([[True, False, False],
              [True, True, True]])

list = [("A",A),("B",B),("C",C)]
for name,i in list:
    print(f"{name}: {np.all(i,axis=1)}")