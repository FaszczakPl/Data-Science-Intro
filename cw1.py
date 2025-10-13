import numpy as np

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

list = [("A",A),("B",B),("C",C),("D",D)]
for name,array in list:
    print(f"{name}:{np.all(array)}")