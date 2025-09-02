#Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso
try: 
    numeros = ('zero',
            'um', 
            'dois', 
            'três', 
            'quatro', 
            'cinco', 
            'seis', 
            'sete', 
            'oito', 
            'nove', 
            'dez', 
            'onze', 
            'doze', 
            'treze', 
            'quatorze', 
            'quinze')

    n = int(input('Digite um número: '))

    print(numeros[n])

except IndexError:
    print('Número inválido, digite um número entre 0 e 15')