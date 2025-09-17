import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sns.set_style('whitegrid')
titanic = pd.read_csv('Titanic-Dataset.csv')
print(titanic.head())
print(titanic.info())

sns.histplot(x='Fare', data=titanic, color='red', bins=30)


sns.despine(left=None, top=None)
plt.show()