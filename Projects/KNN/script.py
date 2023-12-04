import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Lectura de los datos de países
codigo_paises = pd.read_csv('WDICountry.csv', usecols=['Country Code', 'Short Name', 'Income Group'])

# Lectura del segundo archivo con los indicadores
info_paises = pd.read_csv('WDICSV.csv', usecols=['Country Code', 'Indicator Name', '2019'])

# Lista de indicadores de interés
indicadoresInteres = ['Life expectancy at birth, total (years)', 'CO2 emissions (metric tons per capita)', 'GDP per capita (current US$)']

# Filtrar el DataFrame para incluir solo los indicadores de interés
info_paises_filtrado = info_paises[info_paises['Indicator Name'].isin(indicadoresInteres)]

# Pivotar info_paises_filtrado para tener indicadores como columnas
info_paises_pivot = info_paises_filtrado.pivot(index='Country Code', columns='Indicator Name', values='2019')

# Combinar los DataFrames paisesElegidos e info_paises_pivot
df_combinado = codigo_paises.merge(info_paises_pivot, on='Country Code', how='left')

# Ahora df_combinado debería tener la forma deseada con una fila por país y columnas para cada indicador
df_combinado = df_combinado.set_index('Country Code').dropna()

conjunto_de_pruebas = df_combinado.sample(n=20, random_state=123)
# df_combinado = df_combinado.drop(conjunto_de_pruebas.index)


# Scatter plot para CO2 emissions vs GDP per capita
plt.figure(figsize=(14, 6))

# Primer subplot
plt.subplot(1, 3, 1)
for group in df_combinado['Income Group'].unique():
    subset = df_combinado[df_combinado['Income Group'] == group]
    plt.scatter(subset['GDP per capita (current US$)'], subset['CO2 emissions (metric tons per capita)'], label=group, alpha=0.6)
plt.xlabel('GDP per capita (current US$)')
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.title('CO2 emissions vs GDP per capita')
plt.legend()

# Scatter plot para GDP per capita vs Life expectancy
plt.subplot(1, 3, 3)
for group in df_combinado['Income Group'].unique():
    subset = df_combinado[df_combinado['Income Group'] == group]
    plt.scatter(subset['GDP per capita (current US$)'], subset['Life expectancy at birth, total (years)'], label=group, alpha=0.6)
plt.xlabel('GDP per capita (current US$)')
plt.ylabel('Life expectancy at birth, total (years)')
plt.title('GDP per capita vs Life expectancy')
plt.legend()


plt.tight_layout()
plt.show()
