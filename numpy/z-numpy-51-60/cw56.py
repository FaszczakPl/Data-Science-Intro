import numpy as np

#moje roz poprzez plik
np.random.seed(42)
A = np.random.randn(10, 4)
np.savetxt("array.txt",A,fmt="%.4f")
B = np.loadtxt("array.txt")
print(B)
print()
#roz poprzez funkcje
np.set_printoptions(precision=4)
print(A)

