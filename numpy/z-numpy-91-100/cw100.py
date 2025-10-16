import numpy as np

np.set_printoptions(suppress=True)
playway_values = np.loadtxt("playway.txt")

flag = playway_values[:,[0]]<playway_values[:,[3]]
flag = flag.astype(int)
playway_values = np.concatenate((playway_values,flag),axis=1)
print(playway_values)