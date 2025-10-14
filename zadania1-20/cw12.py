import numpy as np

#ndarray.reshape(new_shape)

#1roz
tab= np.arange(10,100)
tab= np.ndarray.reshape(tab,(9,10))
print(tab)

print()
#lub 2roz
print(np.arange(10,100).reshape(9,10))