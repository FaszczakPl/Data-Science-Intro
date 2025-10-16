import numpy as np

np.random.seed(30)

x = np.random.randn(10,4)
mu = 100
sigma = np.sqrt(5)
print(sigma*x+mu)