import numpy as np

np.set_printoptions(suppress=True)
playway_values = np.loadtxt("playway.txt")

print(playway_values[playway_values[:,4].argsort()[::-1]][:10])