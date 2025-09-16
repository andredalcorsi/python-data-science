#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa

n1 = 0
n2 = 0
n3 = 0

n1 = int(input('Digite o valor desejado: '))
n2 = int(input('Digite o valor desejado: '))
n3 = int(input('Digite o valor desejado: '))

while True:

    soma = n1+n2+n3
    mult = n1*n2*n3
    maior = 0

    escolha = int(input('Digite o que você deseja fazer:\n'
                        '[1 - SOMAR]\n'
                        '[2 - MULTIPLICAR]\n'
                        '[3 - MAIOR]\n'
                        '[4 - NOVOS NÚMEROS]\n'
                        '[5 - SAIR DO PROGRAMA]'))
    if escolha == 1:
        print(f'A soma dos valores {n1}, {n2} e {n3} é igual a {soma}!')
    elif escolha == 2:
        print(f'A multiplicação dos valores {n1}, {n2} e {n3} é igual a {mult}!')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior número entre {n1}, {n2} e {n3} é igual a {n1}! ')
        if n2 > n3:
            print(f'O maior número entre {n1}, {n2} e {n3} é igual a {n2}! ')
        if n3 > n1:
            print(f'O maior número entre {n1}, {n2} e {n3} é igual a {n3}! ')
    elif escolha == 4:
        n1 = int(input('Digite o valor desejado: '))
        n2 = int(input('Digite o valor desejado: '))
        n3 = int(input('Digite o valor desejado: '))
    else:
        print('Programa finalizado!')
        break