#Calcule o desvio padrão:

import statistics
import numpy as np

lista = [12, 15, 14, 10, 18, 20, 22, 17, 19, 16]

desvio_padrao = statistics.stdev(lista)
print(f"Desvio Padrão: {desvio_padrao:.2f}")

