import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro

datos = pd.read_csv('datos.csv')

print(datos)

datosH = datos.loc[datos['sexo']=='H']
datosM = datos.loc[datos['sexo']=='M']

pesoH = datosH['peso']
print('pesoH: ',shapiro(pesoH))
edadH = datosH['edad']
print('edadH: ',shapiro(edadH))

print("------------------------------------")

pesoM = datosM['peso']
print('pesoM: ',shapiro(pesoM))
edadM = datosM['edad']
print('edadM: ',shapiro(edadM))


plt.subplot(2,2, 1) 
plt.ylim(0, 6)
plt.xlim(40, 80)
datosH['peso'].hist(color="green")
plt.title("Peso-Hombres")

plt.subplot(2,2,2)
plt.ylim(0, 6)
plt.xlim(20, 70)
datosH['edad'].hist(color="green")
plt.title("Edad-Hombres")

plt.subplot(2, 2, 3) 
plt.ylim(0, 6)
plt.xlim(40, 80)
datosM['peso'].hist()
plt.title("Peso-Mujeres")

plt.subplot(2,2,4)
plt.ylim(0, 6)
plt.xlim(20, 70)
datosM['edad'].hist(color="green")
plt.title("Edad-Mujeres")

plt.show()



