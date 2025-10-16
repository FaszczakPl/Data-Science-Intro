import pandas as pd
import numpy as np


s = pd.Series(
index=np.arange(101,110),
data=np.arange(10,100,10),
dtype="float",
)

print(s)



