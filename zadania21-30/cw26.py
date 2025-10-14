import numpy as np

tab = np.zeros((6,6),dtype=int)
print(tab)

tab[::2,::2] = 10
tab[1::2,::2] = 5
print(tab)

