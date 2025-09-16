#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

nome_prod = " "
mais_barato = None
total_compra = 0
mais_mil = 0
continuar = " "
preco_prod = 0

while True:
    nome_prod = input('Digite o nome do produto: ')
    preco_prod = float(input('Digite o preço do produto: '))

    total_compra+=preco_prod

    if preco_prod >= 1000:
        mais_mil+=1

    if mais_barato is None or preco_prod < mais_barato:
        mais_barato = preco_prod
        nome_barato = nome_prod

    continuar = input('Deseja continuar? ').strip().upper()[0]

    if continuar == 'N':
        print('------------------------------------------------------------------------------------')
        print(f'Total Gasto Na Compra: {total_compra}')
        print(f'Produtos que custam mais de R$1000.00: {mais_mil}')
        print(f'Produto mais barato é {nome_barato}, custando R${mais_barato}!')
        break

