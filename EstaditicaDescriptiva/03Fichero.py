import pandas as pd

#vamos hacer un ejemplo de carga de archivo y aplicar min,max,media,desviacion estandar

def cotizacion(fichero):
    df = pd.read_csv(fichero,sep=";",decimal=",",thousands=".",index_col=0)
    return pd.DataFrame([df.min(),df.max(),df.mean(),df.std()],index=["Minimo","Maximo","Media","Desviacion estandar"])

print(cotizacion('./EstaditicaDescriptiva/cotizacion.csv'))    