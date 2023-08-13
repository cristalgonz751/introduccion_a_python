"""
Escribir una función que reciba por parámetro un valor que representa una cantidad de
segundos, y devuelva el equivalente en {días, horas, minutos, segundos}.
Devolver los valores en el orden indicado.
Probar la función mediante el uso de doctest, teniendo en cuenta los siguientes casos:
>>> equivalente_dhms(3600)
(0, 1, 0, 0)
>>> equivalente_dhms(3666)
(0, 1, 1, 6)
>>> equivalente_dhms(86400)
(1, 0, 0, 0)
>>> equivalente_dhms(90061)
(1, 1, 1, 1)
>>> equivalente_dhms(60)
(0, 0, 1, 0)
>>> equivalente_dhms(1)
(0, 0, 0, 1)
>>> equivalente_dhms(31536000)
(365, 0, 0, 0)
>>> equivalente_dhms(31557600)
(365, 6, 0, 0)

"""
def equivalente_dhms(dhms):
    dias=dhms//86400
    horas=(dhms%86400)//3600
    minutos=((dhms%86400)%3600)//60
    segundos=(((dhms%86400)%3600)%60)
    return (dias,horas,minutos,segundos)
  
print(equivalente_dhms(int(input("ingresar cantidad en segundos:"))))
import doctest
print (doctest.testmod()) 
