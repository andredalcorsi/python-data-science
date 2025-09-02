#Faça um programa que leia um número e retorne o fatorial!

#4! = 4 x 3 x 2 x 1

numero = int(input('Digite um número: '))
fatorial = 1
contador = 1

while contador  > numero + 1:

    fatorial = numero * fatorial

    contador+=1

    print(fatorial)
