import numpy as np

v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])


x = np.dot(v1+v2,v1+v2) == np.dot(v1,v1) + np.dot(v2,v2)
print(x)