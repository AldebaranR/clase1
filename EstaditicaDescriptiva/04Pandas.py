import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./EstaditicaDescriptiva/housing.csv')

#mostrar las primeras 5 filas
print(df.head())

#las ultimas 5 filas
print(df.tail())

#quiero una fila en especifico 
print(df.iloc[7])

#quiero una columna por su nonbre
print(df["ocean_proximity"])

#obtener la media de la columna de total de cuarto
mediacuartos = df["total_rooms"].mean()

#obtener la mediana de la columna population
medianapopularidad = df ["population"].median()
print ('Mediana de popularidad:',medianapopularidad)
std_age = df ["housing_median_age"].std()
print("Desviacion Estandar en años:"  ,
      std_age)

#para poder filtrar
filtrodeloaceano =df[df["ocean_proximity"]=="ISLAND"]
print('Filtro de proximidad del oceano',filtrodeloaceano)

#vamos a crear un grafico de dispercion entre los registros de la proximidad del oceano vs los precios

plt.scatter(df["ocean_proximity"][:10],df["median_house_value"][:10])

#hay que definir a x y 

plt.xlabel("Proximidad")
plt.ylabel('Precio')

plt.title('Grafico de Dispersion de Proximidad al oceano vs el Presio')
plt.show()