import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sns.set_style('whitegrid')

titanic = pd.read_csv('Titanic-Dataset.csv')
print(titanic.head())
print(titanic.info())

sns.boxplot(y='Age', x='Pclass',data=titanic, hue='Pclass', palette='coolwarm')
plt.ylabel('age')

plt.xticks([0,1,2], ['First', 'Second Class', 'Third'])
plt.show()