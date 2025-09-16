import pandas as pd 
import numpy as np 

#1.Escreva um programa que leia, nome, idade, sexo e país de orígem. 

#2. Organize cada leitura como uma lista, e insira em outra lista de armazenamento. 

#3. Após isso, crie um data frame usando pandas com suas respectivas colunas.

#4. Calcule usando pandas.
	#4.1 média de idade
	#4.2 moda de idade
	#4.3 mediana da idade


nome = []
idade = []
sexo = []
pais = []

while True: 

    nome.append(input('Digite o nome: '))
    idade.append(int(input('Digite a idade: ')))
    sexo.append(input('Digite o sexo [M/F]: ').strip().upper()[0])
    pais.append(input('Digite o país de origem: '))
    continuar = input('Deseja continuar? [S/N]: ').strip().lower()[0]

    if continuar == "n":
        break

df = pd.DataFrame({"Nome": nome, "Idade": idade, "Sexo": sexo, "País": pais})

print(df)

print('A média da idade é ', df['Idade'].mean())
print('A moda da idade é ', df['Idade'].mode())
print('A mediana da idade é ', df['Idade'].median())