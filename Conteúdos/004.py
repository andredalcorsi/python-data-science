#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo sem considerar os espaços
#Quantas letras tem o primeiro nome


nome = str(input('Digite seu nome: ')).strip()
sem_espaco = nome.replace(" ", "")
encontra_primeiro = nome.find(' ')



print(nome.upper())
print(nome.lower())
print(len(sem_espaco))
print(encontra_primeiro)