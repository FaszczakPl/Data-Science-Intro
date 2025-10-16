import numpy as np

dat = np.arange('2021-01','2022-01',dtype='datetime64[M]')
A = dat.reshape(-1,3)
print(A)