import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

data= pd.read_csv("IPL Matches 2008-2020.csv") 
sns.barplot(x=data['umpire1'].value_counts().head(10).index ,y=data['umpire1'].value_counts().head(10).values,data=data)
ax=plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title("Top 10 Umpire")
plt.xticks(rotation=90)
plt.show()
