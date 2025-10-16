import pandas as pd

series = pd.Series(['001', '002', '003', '004'], list('abcd'))

print(series.astype(int))