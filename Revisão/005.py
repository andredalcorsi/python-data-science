#Crie um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra “a”
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece na última vez

frase = str(input('Digite sua frase: ')).strip().lower()

frase.replace('ã','a')

frase.replace('á','a')
frase.replace('à','a')
frase.replace('â','a')
frase.replace('ã','a')
frase.replace('ä','a')

print(frase.count('a'))
print(frase.find('a'))
print(frase.rfind('a'))