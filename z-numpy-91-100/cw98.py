import numpy as np

playway_values = np.loadtxt("playway.txt")
np.set_printoptions(suppress=True)

print(playway_values[playway_values[:,3]>300])

