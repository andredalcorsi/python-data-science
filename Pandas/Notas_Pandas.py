#Pandas
#https://pandas.pydata.org/docs/user_guide/merging.html

import pandas as pd
import numpy as np

from numpy.random import randn
'''
#Série
#1
etiqueta = ['a', 'b', 'c']
dados = [10, 20, 30]

serie_1 = pd.Series(data = dados, index= etiqueta)
print(serie_1)

#2
d = {'a': 10, 'b': 20, 'c': 30}
serie_2 = pd.Series(data=d)
print(serie_2)

#Medalhas em Série
ser1 = pd.Series(data= [1,2,3,4], index=['EUA', 'Alemanha', 'Italia', 'Japão'])
ser2 = pd.Series(data= [4,3,2,1], index=['EUA', 'Alemanha', 'Italia', 'Japão'])
ser3 = ser1 + ser2
print(ser3)
print(ser3['EUA'])


#Data Frame
'''
np.random.seed(101)

df = pd.DataFrame(randn(5, 4),
                  ['A', 'B', 'C', 'D', 'E'],
                  ['W', 'X', 'Y', 'Z'])

#print(df)

'''
#1 Linhas - Listas com listas por frequência

base = [['João', 54, 'M'],
        ['Maria', 45, 'F'],
        ['Thiago', 15, 'M'],
        ['Sabrina', 25, 'F']]
#df = pd.DataFrame(data = base, columns= ['Nome', 'Idade', 'Sexo'])
#print(df)
#2 Dicionários - Cada valor será uma lista com todos os registros
base_dic = {'Nome': ['João', 'Maria', 'Thiago', 'Sabrina'],
            'Idade': [50,45,15,25],
            'Sexo': ['M', 'F', 'M', 'F']}
#df = pd.DataFrame(data = base_dic)
#print(df)
#Acesso ao conteúdo
print('-----------------------')
print(df['W'])
print('-----------------------')
print(df[['W', 'X']])
print('-----------------------')
#Acesso a linhas
print(df.loc['A'])
print('-----------------------')
print(df.iloc[0])

#Acesso a valores únicos
idade = df.loc['B', 'X']
print(idade)
idade_2 = df.iloc[1, 1]
print(idade_2)


#Partes de valores
parte_1 = df.loc[['A', 'B'], ['X', 'Y']]
print(parte_1)


#Novas Colunas
df['Nova'] = df['W'] + df['X']
print(df)

#Remover Colunas
df.drop('W', axis=1, inplace=True)
print(df)
df.drop('E', axis=0, inplace=True)
print(df)

#Seleção Condicionada
selec_cond = df['W'] > 0
#print(selec_cond)
selec_cond_2 = df[df['W'] > 0]
#print(selec_cond_2)

#colunas interligadas
coluna_z_coluna_x_maior_que_0 = df['Z'][df['X'] > 0]
#print(coluna_z_coluna_x_maior_que_0)

#Colunas inteligadas com lógica E
coluna_z_coluna_x_e_y_maiores_que_0 = df[(df['X'] > 0) & (df['Y'] > 0)]
print(coluna_z_coluna_x_e_y_maiores_que_0)


#Dados faltantes
d = {'A': [1,2,np.nan], 'B': [5, np.nan, np.nan], 'C': [1,2,3]}
df = pd.DataFrame(data=d)

print(df)
#print(df.isnull())
#print(df.isnull().sum())

#Linha Vazia
#print(df.dropna())
#Coluna Vazia
#print(df.dropna(axis=1))
#print(df.dropna(axis=1, thresh=2))
#print(df.fillna(value=0))

#Estatística
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df['W'].mean())
print(df['W'].median())
print(df['W'].mode())
print(df['W'].std())
print(df['W'].var())
print(df['W'].max())
print(df['W'].min())
print(df['W'].quantile(0.25))
print(df['W'].quantile(0.75))
print(df['W'].value_counts())
print(df['W'].unique())
print(df['W'].nunique())
print(df[['W', 'Z']].cov())
print(df[['W', 'Z']].corr())
print(df.sort_values('W', ascending=False))


def vezes2(x):
    return x * 2

print(df['W'].apply(vezes2))
print(df['W'].apply(lambda x : x * 2))
'''

#Importação de dados
df = pd.read_excel('Base Aula 002 - Exemplo .xlsx')
#df = pd.read_csv('dados_pacientes.csv')
#df = pd.read_html('https://fdic.gov/bank-failures/failed-bank-list')


#df['NOVA'] = df['Peso'] * 10
#print(df.info())
#df.to_excel('Nova_planilha.xlsx')

#print(df[['Vendedor', 'Total']].groupby('Vendedor').sum())
print(df[['Vendedor', 'Total', 'Produto']].groupby(['Vendedor', 'Produto']).sum())









