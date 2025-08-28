#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

#Saída esperada:

#A sua média final é: 5

notas = 0
contador = 0

for contador in range(6):

    nota = float(input('Insira sua nota aqui: '))
    notas+=nota

    contador += 1

    media = notas / 6

print(f'A sua média final é: {media}')