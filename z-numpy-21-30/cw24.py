import numpy as np

tab = np.arange(12).reshape(-1,4)

print(tab[[-1,1,0]])
#2 roz odwrocenie tab
print(tab[::-1])
