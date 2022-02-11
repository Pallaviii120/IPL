
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('IPL Matches 2008-2020.csv')
temp_series =df.toss_decision.value_counts()

labels = (np.array(temp_series.index))

sizes = (np.array((temp_series/temp_series.sum())*100))
colors = ['HotPink','SkyBlue']
plt.pie(sizes,labels = labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)

plt.title("Toss decision Percentage")
plt.show()