#Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele em três disciplinas: matemática, português e história.
#Em seguida, exiba a média das notas dos alunos.

notas = {}

notas_df = []

while True:

    notas['Alunos'] = input('Digite o nome do aluno [Digite sair para terminar o programa]: ').lower()

    if notas['Alunos'] == 'sair':
        print('Programa encerrado com sucesso!')
        break

    notas['Nota de Matemática'] = float(input('Digite a nota de Matemática: '))
    notas['Nota de Português'] = float(input('Digite a nota de Português: '))
    notas['Nota de História'] = float(input('Digite a nota de História: '))
    notas_df.append(notas.copy())

for notas['Alunos'] in notas_df:

    media = (notas_df['Nota de Matemática'] + notas_df['Nota de História'] + notas_df['Nota de Português']) / 3

print(media)



