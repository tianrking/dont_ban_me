import pandas as pd

df = pd.read_csv('final.csv')
print(df.describe())
print(df.shape)