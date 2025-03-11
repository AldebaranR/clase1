import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV (asegúrate de que la ruta del archivo sea correcta)
housing = pd.read_csv('./EstaditicaDescriptiva/housing.csv')

# Estadísticas descriptivas para 'median_house_value'
mean_value = housing['median_house_value'].mean()

# Gráfico de barras para comparar 'median_house_value' con 'population'
plt.figure(figsize=(12, 6))
sns.barplot(x=housing['population'], y=housing['median_house_value'], color='skyblue')

# Añadir una línea roja que marque el promedio de median_house_value
plt.axhline(mean_value, color='red', linestyle='-', label=f'Promedio: {mean_value:.2f}')

# Configurar el gráfico
plt.title('Comparación de median_house_value con population y Promedio')
plt.xlabel('Population')
plt.ylabel('Median House Value')
plt.legend()

# Mostrar el gráfico
plt.show()
