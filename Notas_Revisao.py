'''
 Operações em Python

print(1 + 1)
print(2 - 6)
print(60000/3)
print(99875 * 56)
print(2 ** 3)

# Texto
print('Olá Mundo!')

#Variáveis
a = 5
b = 4
print(a + b)
print(a - b)
c = (a + b) / 5
print(c)

#print formatado
print(f'A soma de a e b é {c}')

#Entrada de dados
nome = input('Digite o nome: ')
idade = input('Digite a sua idade: ')

print(f'Seu nome é {nome} e você tem {idade} anos')

#Inteiro
idade_joao = int(input('João, quantos anos você tem? '))
idade_felipe = int(input('Felipe, quantos anos você tem? '))

soma_idades = idade_joao + idade_felipe

print(f'A soma das idades é {soma_idades}')

#Strings
Nome = 'Luis Eulálio'
#Fatiamento
print(Nome[0])
print(Nome[3:7])

#transformação
print(Nome.upper())
print(Nome.lower())
print(len(Nome))

#Contar
print(Nome.count('a'))
Nome = Nome.replace('l', 'p')
print(Nome)

Nome = input('Digite seu nome: ').strip()
print(Nome)

Nome = input('Digite seu nome: ').split()
print(Nome)
print(Nome[0])

#Find
frase = input('Digite a sua frase: ')
print(frase.find('e'))
print(frase.rfind('e'))



#Condicionais
altura = float(input('Digite a sua altura: '))

#1
if altura > 3:
    print('Cuidado!! Vai bater a cabeça :/ ')
else:
    print('Pode andar no brinquedo')

#2
if altura > 3:
    print('Cuidado!! Vai bater a cabeça :/ ')

elif altura < 1:
    print('Quem sabe ano que vem! ')

else:
    print('Pode andar no Brinquedo')

#E
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))

if altura > 1 and idade > 14:
    print('Você pode andar')
else:
    print('Quem sabe ano que vem')


import random

aleatorio = random.randint(1,10)
print(aleatorio)


for ele in range(0, 1000):
    print("*")

for ele in range(0,10):
    print(ele)

for ele in range(0,10,2):
    print(ele)

for ele in range(10, 0, -1):
    print(ele)

soma = 0
for ele in range(0,11):
    soma = soma + ele


#while

contador = 0

while contador < 100:
    print('Oi')
    contador += 1


# Strings
resposta = ''

while resposta != 'N':
    print('Seja bem vindo')
    resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]


menu = ''

while menu != 4:
    menu = int(input('Digite o menu:'
                     '\n1. Novos Valores'
                     '\n2. Área'
                     '\n3. Volume '
                     '\n4. Sair -> '))

    if menu == 1:
        raio = float(input('Digite o raio: '))

    elif menu == 2:
        print(f'A área é {3.1415 * raio ** 2}')

    elif menu == 3:
        print(f'O volume é {(4/3)* 3.1415 * raio ** 3}')

while True:
    n = input('digite um número[0000 para sair]: ')

    if n == '0000':
        break

while True:
    try:
        numero = int(input('Digite um numero: '))
        x = 10 / 0

    except ValueError:
        print('Só aceitamos números')
    except ZeroDivisionError:
        print('Cuidado ao dividir por 0 ')
    except:
        print('Erro não documentado')
'''
'''

#Funções 

def quebralinha():
    print('-%-'*20)
    
def mensagem (x): 
    quebralinha()
    print(x)
    quebralinha()

def area(x,y): 
    A = x * y
    return A 

quebralinha()
mensagem('Bem-vindo ao Senai')
mensagem('Bem-vindo ao Curso de Python') 
area_do_terreno = area (x = 5, y = 7)
print(area_do_terreno)

#Tuplas 

carro = ('Ferrari', 'Vermelha', 2025)

#Fatiamento 

print(carro)
print(carro([0])
print(carro[0:2])
print(carro[-1])

#Iteração
for i in carro:
    print(i)

for i in range (0, len(carro)):
print(carro[i])

for pos, carac in enumerate(carro): 
print(f'{pos} - {carac}')

idades = (8,9,52,32,66,77,100,2)

print(max(idades))
print(min(idades))
print(sum(idades))
print(len(idades))
print(sum(idades) / len(idades))
print(sorted(idades))
print(sorted(idades, reverse = True))

'''