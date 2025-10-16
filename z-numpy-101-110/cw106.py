import numpy as np
 
 
A = np.array([[4, 3, 6],
              [5, 2, 7],
              [8, 3, 10],
              [3, 4, 2]])
 
def stan(column):
    max_val = max(column)
    min_val = min(column)
    return (column - min_val) / (max_val - min_val)
 
print(np.apply_along_axis(stan, 0, A))