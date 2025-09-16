# Escreva um programa que crie uma lista com varios números lidos pelo usuário, em seguida, exiba apenas os números ímpares da lista.

n = []
while True:

    n.append(int(input('Digite seu número aqui: ')))

    for i in n:
        if i % 2 != 0:
            print(n)
            n.append(int(input('Digite seu número aqui: ')))
        else:
            print('O número tem que ser ímpar!')
    break

