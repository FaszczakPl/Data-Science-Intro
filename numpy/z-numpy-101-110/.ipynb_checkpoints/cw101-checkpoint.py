import numpy as np

A = np.array([[5,-3],[1,-2]])
B = np.array([21,7])

x = np.linalg.solve(A,B)
print("x = ",x[0].astype(float),"y = ",x[1].astype(float))