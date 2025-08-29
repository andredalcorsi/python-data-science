#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

maior_peso = None
menor_peso = None

for contador in range(1,8):
    peso = float(input('Digite seu peso: '))

    if maior_peso == None and menor_peso == None:
        menor_peso = peso
        maior_peso = peso

    if (peso > maior_peso):
        maior_peso = peso

    if (peso < menor_peso):
        menor_peso = peso

print(f'O maior peso é: {maior_peso}kg.')
print(f'O menor peso é: {menor_peso}kg.')