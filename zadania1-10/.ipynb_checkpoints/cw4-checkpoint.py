import numpy as np

A = np.array([[0, 0, 0],
              [0, 0, 0]])
 
B = np.array([[0, 0, 0],
              [0, 1, 0]])
 
C = np.array([[False, False, False],
              [True, False, False]])
 
D = np.array([[0.1, 0.0]])

list=[("A",A),("B",B),("C",C),("D",D)]

for name,i in list:
    print(f"{name}:{np.any(i,axis=0)}")
    