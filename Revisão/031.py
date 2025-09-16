#Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele em três disciplinas: matemática, português e história.
#Em seguida, exiba a média das notas dos alunos.

notas = {}
nota_df = []

while True:

    notas['Aluno'] = input('Digite o nome do aluno [Digite sair para terminar o programa]: ').strip().lower()[0]

    if notas['Aluno'] == 'sair':
        print('Programa encerrado com sucesso!')
        break

    notas['Nota de Matemática'] = float(input('Digite a nota de Matemática: '))
    notas['Nota de Português'] = float(input('Digite a nota de Português: '))
    notas['Nota de História'] = float(input('Digite a nota de História: '))
    nota_df.append(notas.copy())

for alunos_notas in nota_df:
    media = (alunos_notas['Nota de Matemática'] + alunos_notas['Nota de Português'] + alunos_notas['Nota de História']) / 3
    print(f'A média das notas de {alunos_notas['Aluno'].capitalize()} é igual a {round(media, 2)}.')