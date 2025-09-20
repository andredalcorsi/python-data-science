import pandas as pd

# Carregando o dataset
df = pd.read_csv('winemag-data-130k-v2.csv')

# Removendo a primeira coluna de índice, se presente
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

print(f"Formato original do dataset: {df.shape}")

# Contagem de linhas antes da limpeza
linhas_antes = df.shape[0]

# 1. Removendo títulos em branco (NaN)
df_limpo = df.dropna(subset=['title'])
linhas_apos_dropna = df_limpo.shape[0]
print(f"Linhas removidas por terem título em branco: {linhas_antes - linhas_apos_dropna}")
print(f"Formato após remover títulos em branco: {df_limpo.shape}")

# 2. Removendo títulos duplicados
df_limpo = df_limpo.drop_duplicates(subset=['title'])
linhas_apos_dropduplicates = df_limpo.shape[0]
print(f"Linhas removidas por terem título duplicado: {linhas_apos_dropna - linhas_apos_dropduplicates}")

# Mostrando o formato final do DataFrame limpo
print(f"Formato final após toda a limpeza: {df_limpo.shape}")

import seaborn as sns
import matplotlib.pyplot as plt

# Contar vinhos por país usando o DataFrame LIMPO
contagem_paises_limpo = df_limpo['country'].value_counts()

# Pegar os 10 países com mais vinhos
top_10_paises_limpo = contagem_paises_limpo.head(10)

print("\nTop 10 países (com dados limpos):")
print(top_10_paises_limpo)

# --- Criando o Gráfico ---
sns.set_style("whitegrid")
plt.figure(figsize=(12, 7))

barplot = sns.barplot(x=top_10_paises_limpo.index, y=top_10_paises_limpo.values, palette="viridis")

# Adicionando os valores no topo das barras
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')

plt.title('Top 10 Países por Quantidade de Vinhos (Após Limpeza de Duplicados)', fontsize=16)
plt.xlabel('País', fontsize=12)
plt.ylabel('Quantidade de Rótulos de Vinho', fontsize=12)
plt.xticks(rotation=360)
plt.tight_layout()
plt.show()