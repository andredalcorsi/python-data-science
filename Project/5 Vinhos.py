import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Quais são os 5 países com os vinhos mais bem avaliados?

df = pd.read_csv('winemag-data-130k-v2.csv')

analise = df.groupby('country')['points'].mean()

paises_ordenados = analise.sort_values(ascending=False)
top_cinco = paises_ordenados.head(5)
top_cinco_df = top_cinco.reset_index()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
grafico_format = sns.barplot(x='points', y='country', data=top_cinco_df)

# Adicionar títulos e rótulos
grafico_format.set_title('Top 5 Países por Pontuação Média de Vinhos', fontsize=16)
grafico_format.set_xlabel('Pontuação Média', fontsize=12)
grafico_format.set_ylabel('País', fontsize=12)

plt.show()
