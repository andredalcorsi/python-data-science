import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


gorjeta = sns.load_dataset('tips')
print(gorjeta.head())
print(gorjeta.info())

'''
#Plotagem univariada
sns.histplot(gorjeta['total_bill'], bins=30, kde=True)
plt.show()

#Plotagem Comparada
sns.jointplot(x='total_bill', y='tip', data=gorjeta)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=gorjeta, kind='hex')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=gorjeta, kind='reg')
plt.show()



#Gráficos comparativos para todas as variáveis numéricas
sns.pairplot(gorjeta, hue='sex')
plt.show()

#Rugplot
sns.rugplot(gorjeta['total_bill'])
plt.show()


#kde
sns.kdeplot(gorjeta['total_bill'])
plt.show()

#Plotagem de categorias
sns.barplot(y='sex', x='total_bill', data=gorjeta, color='red', estimator=np.std)
plt.show()

#Gráfico de Contagem
sns.countplot(x='sex', data=gorjeta)
plt.show()


#Diagrama de Caixas
sns.boxplot(x='day', y='total_bill', data=gorjeta)
plt.show()

sns.boxplot(x='day', y='total_bill', data=gorjeta, hue='smoker')
plt.show()

#Diagrama de violino
sns.violinplot(x='day', y='total_bill', data=gorjeta, hue='sex', split=True)
plt.show()


#Stripplot
sns.stripplot(x='day', y='total_bill', data=gorjeta, jitter=True)
plt.show()

#Gráfico de Enxame
sns.swarmplot(x='day', y='total_bill', data=gorjeta)
plt.show()

#Coringa :)
sns.catplot(x='day', y='total_bill', data=gorjeta, kind='bar')
plt.show()

#Plotagem de matriz

voos = sns.load_dataset('flights')

#Mapa de Calor
vp = voos.pivot_table(index='month', columns='year', values='passengers')
#sns.heatmap(vp, cmap='magma')
#plt.show()

sns.clustermap(vp, cmap='coolwarm', standart_scale=1)
plt.show()

'''