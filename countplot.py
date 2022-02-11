
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('IPL Matches 2008-2020.csv')
temp_series =df.toss_decision.value_counts()

plt.figure(figsize=(12,6))
sns.countplot(x='toss_winner',hue='toss_decision',data=df)

plt.xticks(rotation='vertical')
plt.show()