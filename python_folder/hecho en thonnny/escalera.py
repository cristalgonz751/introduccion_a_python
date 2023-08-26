'''
Escribir una función que indique si los 5 dados que han sido arrojados por un jugador, forman escalera.
La función recibirá por parámetro, una tupla, con los 5 valores obtenidos al arrojar los dados.

Deberá devolver True, si forman escalera, de lo contrario, deberá devolver, False. 

Para que se de escalera, hay 3 alternativas: (1,2,3,4,5); (2,3,4,5,6) ó (3,4,5,6,1),
claro que el orden en el que aparecen los valores, no importa.
'''

def ingresa(tirada):
    lista=[]
    for i in range(0,5):
        lista.append(tirada[i])
    return lista

def	ordenar(lista):
    lista.sort()
    return lista

def analizar(tirada):
    '''
    analiza la jugada de 5 dados
    >>> analizar((2,4,2,1,3))
    no se formo escalera
    >>> analizar((5,4,2,1,3))
    salio la escalera [1,2,3,4,5]
    >>> analizar((6,2,4,5,3))
    salio la escalera [2,3,4,5,6]
    >>> analizar((6,4,1,5,3))
    salio la escalera [3,4,5,6,1]
    >>> analizar((6,4,2,3,3))
    no se formo escalera
    '''
    lista=[]
    lista=ingresa(tirada)
    lista=ordenar(lista)
    if lista == [1,2,3,4,5]:
        print('salio la escalera [1,2,3,4,5]')
        return
    elif lista == [2,3,4,5,6]:
        print('salio la escalera [2,3,4,5,6]')
        return
    rolar=lista.pop(0)
    lista.append(rolar)
    if lista == [3,4,5,6,1]:
        print('salio la escalera [3,4,5,6,1]')
        return
    else:
        print('no se formo escalera')
    return

analizar((6,5,2,3,4))

import doctest
print(doctest.testmod())

    
    