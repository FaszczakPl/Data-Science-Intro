import numpy as np

dat = np.arange('2020-01-06','2020-03',dtype='datetime64[D]')

print(dat[::7])
