import pandas as pd
import numpy as np

pref = 'Juan'
peso = np.round(np.random.normal(65, 7, 20))

print(peso)

nombres = list()

for i in range(20):
  nombres.append(pref+str(i))

datos = pd.DataFrame({'nombres':nombres, 'peso':peso})

print(datos.keys())

val = datos.values

print(type(val))

print(datos.info)

edad = np.round(np.random.uniform(40, 70, 20))

datos.insert(1, 'edad', edad)

tiempoInternet = np.round(np.random.uniform(1, 6, 20))

datos['tiempoInternet'] = tiempoInternet

print(datos)

datos2 = datos.iloc[8:12]

print(datos2)

