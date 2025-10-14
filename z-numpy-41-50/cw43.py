import numpy as np

image = np.random.randint(0,256,(200,300,3),dtype=np.uint8)

image_extended = np.expand_dims(image,axis=0)

print(image_extended)