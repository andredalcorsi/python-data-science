'''

1. Importe a Vendas_Incorreto - OK 

2. Trate todos os dados incorretos - OK 

3. Analise estatisticamente o arquivo

'''

import pandas as pd 

file_path = r'C:\Users\andre\OneDrive\Documentos\Senai\python-data-science\Pandas\Vendas_Incorreto.xlsx'

df = pd.read_excel(file_path)

df.dropna(axis=1, how='all', inplace=True)
df.dropna(axis=0, how='all',inplace=True)

df.rename(columns={'Preco': 'Preço de Venda'}, inplace=True)
df.rename(columns={'Devolucao': 'Devolução'}, inplace=True)

print(df.head())
print(df.info())


print(f'A média de Descontos é igual a \n: ', df['Desconto'].median())