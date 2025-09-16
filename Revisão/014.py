#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci


primeiro = 0
segundo = 1
contador = 0
terceiro = 0

n = int(input('Digite um número: '))

while contador < n:

    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro+segundo
    contador+=1

    print(f'{terceiro}')
