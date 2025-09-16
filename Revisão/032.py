#Crie um programa que leia o nome, sexo e idade de vários Alunos, guardando os dados de cada aluno em um dicionário e todos os dicionários em uma lista.
#No final mostre:

#Quantas pessoas foram cadastradas
#A média de idade do grupo
#Uma lista com todas as mulheres
#Uma lista com todas as pessoas com idade acima da média

alunos = []

while True:

    nome = input('Nome[fim para parar]: ')
    if nome == 'fim':
        break
    sexo = input('Sexo[M/F]: ').strip().upper()[0]
    idade = int(input('Idade: '))


    alunos.append({'nome': nome, 'sexo': sexo, 'idade': idade})

    #Quantas pessoas foram cadastradas
    num_cadastrados = len(alunos)

    #A media de idade do grupo

    soma_idades = sum(aluno['idade'] for aluno in alunos)
    media_idades = soma_idades / num_cadastrados

    #Uma lista com todas as mulheres

    mulheres = [aluno['nome'] for aluno in alunos if aluno['sexo'] == 'F']

    #uma lista com todas as pessoas com idade acima da media
    acima_media = [aluno['nome'] for aluno in alunos if aluno['idade'] > media_idades]


    print(f'Número de pessoas cadastradas: {num_cadastrados}\n'
          f'Média de idades: {media_idades}\n'
          f'Quantidade de mulheres: {mulheres}\n'
          f'Pessoas com idade acima da média: {acima_media}')
