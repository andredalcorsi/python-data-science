#biblioteca padrão de estatística
import statistics
import numpy as np

#base de dados
lista_1 = [10, 10, 30, 30,40]

#Média, moda e mediana
print(f'média: {statistics.mean(lista_1)},'
      f'\nmoda: {statistics.mode(lista_1)}'
      f'\nmediana: {statistics.median(lista_1)}')

print(f'{np.percentile(lista_1, 10)}')


# Calcular a variância
variancia = statistics.variance(lista_1)
print(f"Variância: {variancia}")

# Calcular o desvio padrão
desvio_padrao = statistics.stdev(lista_1)
print(f"Desvio Padrão: {desvio_padrao:.2f}")


