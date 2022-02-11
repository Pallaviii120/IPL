
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('IPL Matches 2008-2020.csv')
plt.figure(figsize=(12,6))
sns.countplot(x='venue',data=df)
plt.xticks(rotation='vertical')
plt.plot()
plt.show()