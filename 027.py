# Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas listas.
# Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].

l1 = []
l2 = []

for i in range(5):
    try:
        l1.append(int(input('N: ')))
        l2.append(int(input('N: ')))

    except ValueError:
        print('Aceitamos apenas números.')
l3 = []
for i in range (5):
    l3.append(l1[i]+l2[i])

print(l3)



