import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df.head())
print(df.tail())

print(df.shape) #will give(x,y) x=cols y=rows
print(df.columns)

#lets get a specific column using the column key
height = df['Height']
print(height)
print(height.describe())# returns descriptive statisical information
#can be also used on dataframes
print(df.describe())
