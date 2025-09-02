#Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

#Apenas os 3 primeiros mais assistidos
#Os últimos 2 mais assistidos
#A lista em ordem alfabética
#Em que posição está “O rei leão”

filmes = ('Avatar', 'Vingadores: Ultimato', 'Avatar: O Caminho da Água', 'Titanic', 'Star Wars: O Despertar da Força', 'Vingadores: Guerra Infinita', 'Homem-Aranha: Sem Volta Para Casa','Divertida Mente 2', 'Jurassic World', 'Rei Leão')


print(filmes[0:3])
print(filmes[-2:])
print(sorted(filmes))
print(filmes.index('Rei Leão'))