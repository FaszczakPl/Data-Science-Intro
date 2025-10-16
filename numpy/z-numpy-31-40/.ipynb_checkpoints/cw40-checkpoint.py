import numpy as np

image = np.random.randint(0,256,(200,300),dtype=np.uint8)

image_sorted = np.sort(image,axis=1)

print(image_sorted)