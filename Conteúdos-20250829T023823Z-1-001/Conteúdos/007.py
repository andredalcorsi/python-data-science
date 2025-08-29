#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

letra = str(input('Digite uma letra: ')).strip().lower()

vogal = ['a', 'à', 'á', 'ã', 'ä', 'â', 'e', 'é', 'è', 'ê', 'ë', 'i', 'í', 'ì', 'ï', 'ó', 'ö', 'ô', 'ú', 'ü', 'û']

if letra in vogal:
    print('Vogal!')
else:
    print('Consoante!')