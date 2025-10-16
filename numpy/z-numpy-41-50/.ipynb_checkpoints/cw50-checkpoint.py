import numpy as np

image = np.random.randint(0,256,(10, 10, 3),dtype=np.uint8)

result = image[:5,:5,:]
print(result)