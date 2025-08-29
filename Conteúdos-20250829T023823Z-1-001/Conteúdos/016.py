#Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
#Ao final deve mostrar a quantidade de vitórias.


import random


escolha_pc = random.randint(1, 11)
escolha_usuario = int(input('Escolha um número de 1 a 10: '))
escolha_par_impar = int(input('Escolha entre par ou ímpar: '))

par = 0
impar = 1
while True:

    soma_escolhas = escolha_pc + escolha_usuario

    if escolha_par_impar == 0:
        print('Você escolheu par!')
    else:
        print('Você escolheu ímpar!')

    if escolha_usuario % 2 == escolha_par_impar:
        print('Você venceu')
    else:
        print('Você perdeu.')
    break