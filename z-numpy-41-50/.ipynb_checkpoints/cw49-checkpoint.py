import numpy as np

np.random.seed(42)

image = np.random.randint(0,256,(10, 10, 3),dtype=np.uint8)


print(image[:,:,0])