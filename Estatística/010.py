
#Calcule o primeiro e o terceiro quartis:

import statistics
import numpy as np


lista = [12, 15, 14, 10, 18, 20, 22, 17, 19, 16, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

primeiro_quartil = 25/100 * (20+1)
terceiro_quartil = 75/100 * (20+1)


print(f'{np.percentile(lista, 25)}')
print(f'{np.percentile(lista, 75)}')