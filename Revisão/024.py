#Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso
try: 
    numero_str = ('zero',
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

    numero_int = int(input('Digite um número: '))

    print(numero_str[numero_int])

except IndexError:
    print('Número inválido, digite um número entre 0 e 15')
except ValueError:
    print('Valor inválido, digite um número entre 0 e 15')