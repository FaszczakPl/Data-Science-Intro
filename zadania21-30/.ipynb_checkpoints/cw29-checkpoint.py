import numpy as np

#tworzenie tab 1
A = np.array([[5, 1, 2, 1, 2],
       [9, 1, 9, 7, 5],
       [4, 1, 5, 7, 9]])
#tworzenie tab za pomoca random

np.random.seed(10)
B = np.random.randint(1,10,(3,5))

print(np.unique(A))