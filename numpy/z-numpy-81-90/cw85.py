import numpy as np

A = np.array([['#summer#time#mood'],
              ['#sport#time']])

A = np.char.replace(A,"#"," ")
A = np.char.strip(A)
print(A)