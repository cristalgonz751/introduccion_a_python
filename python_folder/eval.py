'''
Realizá las siguientes operaciones y luego ingresá el resultado en el cuadro
 Crea una lista de valores enteros entre 1000 y 1123, inclusive; en orden decreciente
 Reemplazá en la lista los valores que sean múltiplos de 5, por 10 si son menores a 1050, sino por 15
 Eliminá de la lista todos los valores que se encuentran en las posiciones pares
 Generá una nueva lista ordenada en forma creciente (no pierdas la que venís usando)
 Indicá en el cuadro Respuesta que está debajo, cuántos elementos que ocupan la misma posición en ambas listas, son iguales
'''


lista = [i for i in range(1123, 999, -1)]
for pos in range(0,len(lista)):
    if lista[pos] % 5==0 and lista[pos] < 1050:
        lista[pos]=5
    elif lista[pos] % 5==0 and lista[pos] >= 1050:
        lista[pos]=15
lista=lista[0::2]
lista2=sorted(lista)
for pos in range(0,len(lista)):
    contador=0
    if lista[pos]==lista2[pos]:
        contador+=1
# print(lista)
# print(lista2)
# print(contador)

