#Como a quantidade de vinhos varia entre os diferentes países?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('winemag-data-130k-v2.csv')

analise = df.groupby('country')['country'].count()
print(analise)
analise_dois = df.groupby('province')['province'].count()
print(analise_dois)