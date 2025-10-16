import numpy as np

A = np.array([[4, 3, 6],
              [5, 2, 7],
              [8, 3, 10],
              [-3, 4, 2]])

print(np.apply_along_axis(np.max,0,A)-np.apply_along_axis(np.min,0,A))