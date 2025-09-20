import pandas as pd


df = pd.read_excel('winemag-data-130k-v2.xlsx')

print(df.head())
print(df.info())