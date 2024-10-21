import pandas as pd
import numpy as np

prefH = 'Juan'
pesoH = np.round(np.random.normal(65, 7, 20))
edadH = np.round(np.random.uniform(40, 60, 20))
sexoH = ['H']*20

nm = 18
prefM = 'Maria'
pesoM = np.round(np.random.normal(60, 5, nm))
edadM = np.round(np.random.uniform(40, 60, nm))
sexoM = ['M']*nm

sexo = sexoH + sexoM

juanes = []
for i in range(20):
  juanes.append(prefH+str(i))

marias = []
for i in range(nm):
  marias.append(prefM+str(i))

nombres = juanes + marias

peso = np.concatenate((pesoH, pesoM))

edad = np.concatenate((edadH, edadM))

datos = pd.DataFrame({'nombres':nombres, 'sexo':sexo, 'peso':peso, 'edad':edad})
print(datos)

datos = datos.sample(n=38)

datos.to_csv('datos.csv', index=False)





