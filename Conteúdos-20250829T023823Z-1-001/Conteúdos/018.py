#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

nome_prod = ""
mais_barato = 0
total_compra = 0
mais_mil = 0
contador = 0

while True:


    prod = input('Digite o nome do produto: ')
    preco_prod = float(input('Digite o preço do produto: '))

    total_compra+=preco_prod

    if preco_prod > 1000:
        mais_mil+=1
    if (preco_prod < mais_barato):
        mais_barato = preco_prod
        nome_barato = nome_prod

    contador +=1

    continuar = ' '

    while continuar not in 'SN':
            continuar = input('Deseja continuar? ').strip().lower()[0]
    if continuar == 'N':
        break

print('------------------------------------------------------------------------------------')
print(f'Total Gasto Na Compra: {total_compra}\n'
      f'Produtos que custam mais de R$1000.00: R${mais_mil}\n'
      f'Produto mais barato é {nome_barato}, custando R${mais_barato}! ')

