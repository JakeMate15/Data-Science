import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

paises = pd.read_csv('infoPaises.csv', index_col = 0)

co2 = paises['CO2 emissions (metric tons per capita)']
gdp = paises['GDP per capita (current US$)']
es = paises['Life expectancy at birth, total (years)']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(co2, gdp, es)

ax.set_xlabel('Emisiones de CO2 (toneladas métricas per cápita)')
ax.set_ylabel('PIB per cápita (US$)')
ax.set_zlabel('Esperanza de vida al nacer (años)')

plt.show()

