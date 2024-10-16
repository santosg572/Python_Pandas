import pandas as pd
import matplotlib.pyplot as plt

dd = pd.read_csv('dat1.csv')

print(dd)

print(dir(dd))

print(dd.info())

print(dd.keys())

x = dd['nombre']

print(x)

nom = list(x)

print(nom)

dd.boxplot()

plt.show()
