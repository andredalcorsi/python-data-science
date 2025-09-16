#Crie um programa que tenha a função volume(), que receba as dimensões de um cubo mostra o volume do cubo

def volume (x, y, z):
    V = x * y * z
    return V

x = int(input('Defina um lado do quadrado: '))
y = int(input('Defina outro lado do quadrado: '))
z = int(input('Defina a altura: '))

print(volume(x, y, z))
