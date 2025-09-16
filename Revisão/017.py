#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000


contador = 0


while True:

    tabuada = input('Você quer que eu faça a tabuada do [Digite 0000 para sair]: ')

    if tabuada == '0000':
        print('Programa Finalizado!')
        break

    tabuada_str = int(tabuada)

    for contador in range (1,11):

        print(f'{tabuada_str}x{contador}={tabuada_str*contador}')
    contador += 1