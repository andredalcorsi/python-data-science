#Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:

#Quantas pessoas foram cadastradas
#Uma listagem com as pessoas com o maior QI
#Uma listagem com as pessoas de menor QI


pessoas = [[],[]]

while True:

    nome = input('Nome [digite sair para terminar]: ')

    if nome == 'sair':
        break

    pessoas[0].append(nome)
    pessoas[1].append(int(input('QI: ')))

    pessoas_reverso = sorted(pessoas[0], reverse=True)
    qi_reverso = sorted(pessoas[1], reverse=True)
    pessoas_menor_qi = sorted(pessoas[0])
    pessoas_menor = sorted(pessoas[1])

print(f'O número de pessoas cadastradas é igual a {len(pessoas[0])}')

print('*-' *20)
print('PESSOAS DO MAIOR QI PARA O MENOR QI')

for i in qi_reverso:
    print(f'{pessoas[0][pessoas[1].index(i)]} tem QI igual a {pessoas[1][pessoas[1].index(i)]}')
print('*-' *20)
print('PESSOAS DO MENOR QI PARA O MAIOR QI')
for i in pessoas_menor:
    print(f'{pessoas[0][pessoas[1].index(i)]} tem QI igual a {pessoas[1][pessoas[1].index(i)]}')


