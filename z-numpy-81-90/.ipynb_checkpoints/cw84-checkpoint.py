import numpy as np

A = np.array([['PLW CDR 11B TEN', 'AMC LPP'],
              ['CDR PKO KGH', 'CCC QMK']])

print(np.char.split(A,sep=" "))