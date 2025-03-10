#crear una funcion que se encargue de recibir un diccionario de las notas de los estudiantes de analisis de sus datos que van a reprobar y obtener su min,max, media y desviacion estandar 
import pandas as pd
def estadisticas_notas(notas):
    notas = pd.Series(notas)
    estadistica = pd.Series([notas.min(),notas.max(),notas.mean(),notas.std()], index=["Min","Max","Media","Desviacion estandar"])
    return estadistica

notas = {"juan":9,"pedro":5.6,"rosalba":5.5,"jaime":4,"federico":9,}
print(estadisticas_notas(notas))