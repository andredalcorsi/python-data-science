#Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
#Ao final deve mostrar a quantidade de vitórias.


import random

escolha_pc = random.randint(1, 11)
escolha_usuario = int(input('Escolha um número de 1 a 10: '))
escolha_par_impar = int(input('Escolha entre par ou ímpar [0 - PAR | 1 - ÍMPAR]: '))

par = 0
impar = 1
vitorias = 0 

while True:

    soma_escolhas = escolha_pc + escolha_usuario

    if escolha_par_impar == 0:
        print(f'Você escolheu par !')
    else:
        print(f'Você escolheu ímpar!')

    if soma_escolhas % 2 == 0 and escolha_par_impar == 0 or soma_escolhas % 2 != 0 and escolha_par_impar == 1:
        print('Vitória')
        vitorias+=1
    else:
        print(f'Derrota com {vitorias} vitórias!')
    break