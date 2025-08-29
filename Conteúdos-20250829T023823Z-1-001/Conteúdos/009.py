#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.


contador = 0

tabuada = int(input('Digite um número: '))

for contador in range (1,11):

    resultado = tabuada * contador

    print(f'{tabuada}x{contador}={resultado}')
    contador += 1