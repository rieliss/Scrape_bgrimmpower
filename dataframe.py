import pandas as pd

df = df = pd.read_csv("https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv", usecols=range(1,17))

print(df)
print(df.columns)

df2 = df.rename(columns={'year':'years'})
print(df2)