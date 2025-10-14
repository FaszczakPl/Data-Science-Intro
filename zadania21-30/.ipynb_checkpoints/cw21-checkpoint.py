import numpy as np

tab = np.arange(0,12)
tab = np.ndarray.reshape(tab,(3,4))

np.save('array.npy',tab)

B = np.load('array.npy')
print(B)

