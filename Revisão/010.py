#Escreva um programa que calcule a soma dos números de 1 a 100 usando um loop
contador = 0 
soma = 0
import time

for contador in range (5):

    contador+=1
    time.sleep(0.25)

    soma+=contador
    print(contador)
print(f'A soma dos números do contador é igual a: {soma}')
  