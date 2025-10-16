import numpy as np

tab = np.array([[4, 3, 6],
              [5, 2, 7],
              [8, 3, 10],
              [-3, 4, 2]])

print(np.apply_along_axis(sorted,1,tab))
