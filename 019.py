#Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo número. 
#No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.

try:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    resultado = a / b
    print(f'O resultado da divisão é: {resultado}')
except ValueError:
    print('Erro: Por favor, digite apenas números inteiros.')
except ZeroDivisionError:
    print('Erro: Não é possível dividir por zero.')