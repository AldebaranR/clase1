#vamos a crear un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una seria con los datos antes y despues de a plicar el descuento al 10%
import pandas as pd
inicio= int (input('Introdice el año inicial de la ventas :'))
fin = int(input('Introduce el años  final de las ventas:'))
ventas={}
for i in range(inicio,fin+1):
    ventas[1]=float (input('Introduce las ventas del año'+ str (1)+''))
    ventas =pd.Series(ventas)
    print('ventas\n',ventas)
    print('Ventas con Descuento\n',
    ventas*0.9)