import numpy as np

A = np.array([[0.4, 0.3, 0.3], [0.1, 0.1, 0.8], [0.2, 0.5, 0.3]])

#troche inaczej
for i in range(len(A)):
    print(np.argmax(A[i]))

#roz
print(np.argmax(A,axis=1))