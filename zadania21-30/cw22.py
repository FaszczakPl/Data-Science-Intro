import numpy as np

tab = np.arange(12)
tab = np.ndarray.reshape(tab,(3,4))

np.savetxt("array.txt",tab,fmt="%0.2f")

B = np.loadtxt("array.txt")
print(B)