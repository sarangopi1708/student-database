import pandas as pd 
import matplotlib as mpot
import numpy as np      
df = pd.read_csv('/Users/saran/Desktop/googleplaystore.csv')
print(df)
df.head()
df.describe()
print(df.to_string())
