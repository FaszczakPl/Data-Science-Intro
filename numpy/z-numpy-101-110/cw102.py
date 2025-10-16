import numpy as np

A = np.array([[1,1,1],[2,1,5],[1,-1,-1]])
B = np.array([1,0,0])

x = np.linalg.solve(A,B)
x = np.round(x,2)
print("x = ",x[0]," y = ",x[1]," z = ",x[2])