#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

import random

palpite = []
palpites = []

n = int(input('n: '))

for i in range(n):
    for i in range(6):
        aleatorio = random.randint(1,60)
        while aleatorio in palpite:
            aleatorio = random.randint(1,60)
        palpite.append(aleatorio)

    palpites.append(palpite[:])
    palpite.clear()

for i in palpites:
    print(sorted(i))
