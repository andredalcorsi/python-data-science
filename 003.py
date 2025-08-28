#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

import math

#V = (4/3) . π . r³
#A = 4 . π . r²

#Saída esperada:

#Volume da Esfera: Y
#Área da esfera: X

raio = float(input('Digite o raio: '))
pi = 3.14

volume = (4/3) * (pi * (raio**3))
area = (4 * (pi * (raio**2)))

print(f'Volume da Esfera: {volume}\n'
      f'Área da Esfera: {area}')