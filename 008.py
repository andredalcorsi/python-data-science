#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random

papel = 0
pedra = 1
tesoura = 2

computador = random.randint(0, 2)

usuario = int(input('Digite sua jogada! \n'
                    '0 - PAPEL\n'
                    '1 - PEDRA\n'
                    '2 - TESOURA\n'
                    'Inserir: '))

user_str = str(usuario).replace('0', 'Papel').replace('1', 'Pedra').replace('2','Tesoura').upper()
comp_str = str(computador).replace('0', 'Papel').replace('1', 'Pedra').replace('2','Tesoura').upper()
print(f'Você escolheu: {user_str}\n'
      f'Computador escolheu: {comp_str}')

if usuario == computador:
    print('Empate!')
elif (usuario == tesoura and computador == papel) or (usuario == pedra and computador == tesoura) or (usuario == papel and computador == pedra):
    print('Você ganhou!')
else:
    print('Você perdeu!')
