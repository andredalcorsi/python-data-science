'''

1.Importe a Base Aula 002 - Exemplo.xlsx 

2. Encontre a Informação
	2.1 - Qual país vendeu mais(Total)?
	2.2 - Qual o melhor vendedor?
	2.3 - Qual o melhor tipo de loja?
	2.4 - Qual é o tipo de envio mais usado?
	2.5 - Qual o público que mais atendemos (Gênero)?
	2.6 - Quem fez as 3 maiores vendas?
	2.7 - Adicione uma nova coluna comissão (Total * 5%)

'''

import pandas as pd
import numpy as np 

file_path = r'C:\Users\andre\OneDrive\Documentos\Senai\python-data-science\Pandas\Base Aula 002 - Exemplo .xlsx'

df = pd.read_excel(file_path)

print(df)

#2.1 - Qual país vendeu mais(Total)?
print(df[['País', 'Total']].groupby('País')['Total'].sum().sort_values(ascending=False))

#2.2 - Qual o melhor vendedor?
print(f'Os melhores vendedores foram: \n', df[['Vendedor', 'Total']].groupby('Vendedor')['Total'].sum().sort_values(ascending=False))

#2.3 - Qual o melhor tipo de loja?
print(f'Melhor tipo de loja: \n', df[['Loja', 'Total']].groupby('Loja')['Total'].sum().sort_values(ascending=False))

#2.4 - Qual é o tipo de envio mais usado?
print(f'O tipo de envio mais usado: \n', df[['Tipo de Envio', 'Total']].groupby('Tipo de Envio')['Total'].sum().sort_values(ascending=False))

#2.5 - Qual o público que mais atendemos (Gênero)?
print(f'Público mais atendido: \n', df[['Gênero', 'Total']].groupby('Gênero')['Total'].sum().sort_values(ascending=False))

#2.6 - Quem fez as 3 maiores vendas?
print(f'As 3 maiores vendas são de: \n', df[['Vendedor', 'Total']].groupby('Vendedor')['Total'].sum().sort_values(ascending=False).head(3))

#2.7 - Adicione uma nova coluna comissão (Total * 5%)
df['Comissão'] = df['Total'] * 0.05
print(f'As comissões de cada vendedor: \n', df.groupby('Vendedor')['Comissão'].sum().sort_values(ascending=False).head(3))