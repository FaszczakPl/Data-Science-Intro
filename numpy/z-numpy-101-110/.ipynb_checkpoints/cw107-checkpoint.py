import numpy as np

A = np.array([[4, 3, 6],
              [5, 2, 7],
              [8, 3, 10],
              [-3, 4, 2]])
def zmien(row):
    row[0],row[-1] = row[-1],row[0]
    return row
print(np.apply_along_axis(zmien,1,A))