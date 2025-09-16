#Calcule a média aritimética simples, moda, mediana das seguintes notas.

import statistics
import numpy as np

media_aritmetica = [5.7, 6.5, 6.9, 8.3, 8, 4.2, 6.3, 7.4, 6.9]

print(f'média: {round(statistics.mean(media_aritmetica),2)}'
      f'\nmoda: {statistics.mode(media_aritmetica)}'
      f'\nmediana: {statistics.median(media_aritmetica)}')