import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sns.set_style('whitegrid')
df = pd.read_csv('Titanic-Dataset.csv')


sns.jointplot(x='Fare', y='Age', data=df)
plt.ylabel('age')
plt.xlabel('fare')
plt.show()