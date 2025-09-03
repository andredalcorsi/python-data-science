# Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa lista até que ele digite um número negativo.
# Em seguida, exiba a lista na tela.

lista = []

while True:

    try:
        n = (int(input('N[Negativo para sair]: ')))

        if n < 0:
                break
        lista.append(n)
    except ValueError:
        print('Só aceitamos números: ')

print(f'A lista é {lista}')