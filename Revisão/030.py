#Escreva um programa que crie um dicionário com as informações de 5 livros, como título, autor, ano de lançamento e
# número de páginas.
#Em seguida, exiba apenas os autores dos livros.


livros = {}

livros_df = []

for contador in range(5):

    livros['Título'] = input('Título do livro: ')
    livros['Autor'] = input('Autor: ')
    livros['Lançamento'] = int(input('Ano de Lançamento: '))
    livros['Páginas'] = int(input('Número de Páginas: '))
    livros_df.append(livros.copy())

for i in range(len(livros_df)):
    print(f'Lista de autores: {livros_df[i]['Autor']}')