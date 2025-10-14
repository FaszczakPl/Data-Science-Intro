import numpy as np

np.random.seed(30)

x = np.random.randn(10,4)
mu = 100
sigma = np.sqrt(5)
print(sigma*x+mu)

#mu – średnia, wokół której liczby się skupiają
#sigma – odchylenie standardowe, czyli jak bardzo wartości są rozproszone
#x – liczba z rozkładu standardowego N(0,1)