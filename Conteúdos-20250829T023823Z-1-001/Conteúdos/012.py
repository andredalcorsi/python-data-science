#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
#e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.

import random

contador = 0
pc = random.randint(1, 11)
adivinha = int(input('Digite um número entre 1 e 10: '))

while True:


    if adivinha != pc:
        print('Você errou! Tente novamente.')
        adivinha = int(input('Digite um número entre 1 e 10: '))
        contador += 1

    if adivinha == pc:
        print('Você acertou!\n'
              f'Número de tentativas: {contador+1} ')
        break

