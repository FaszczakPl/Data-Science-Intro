import numpy as np

tab = np.full((4,4),1,dtype=float)
print(tab)
tab = np.pad(tab,pad_width=1,mode="constant",constant_values=0)
print()
print(tab)
