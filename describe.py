import pandas as pd
df=pd.read_csv('IPL Matches 2008-2020.csv')
var=df.describe()
print("Describe of dataset: ")
print(var)