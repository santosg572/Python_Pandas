import pandas as pd

datos = pd.read_csv('datos.csv')

print(datos)

datosH = datos.loc[datos['sexo']=='H']

print(datosH)

print(datos.describe(include='all'))



