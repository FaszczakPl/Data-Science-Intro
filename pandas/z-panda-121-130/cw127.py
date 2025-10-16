import pandas as pd
 
 
stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)
new_item = pd.Series({'BBT':25.5,'F51':19.2})
quotations = pd.concat([quotations,new_item])
print(quotations)