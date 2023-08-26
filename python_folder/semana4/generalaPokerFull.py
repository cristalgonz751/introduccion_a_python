'''
De igual modo que el ejercicio anterior (Dados Escalera), escribir una función
 para cada uno de los posibles casos:
Generala: 5 dados de igual valor
Póker: 4 dados iguales y 1 distinto
Full: 3 dados iguales y otros 2 iguales

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
    'no se formo Generala,Poker ni Full'
    >>> analizar((5,4,2,1,3))
    'no se formo Generala,Poker ni Full'
    >>> analizar((6,2,4,5,3))
    'no se formo Generala,Poker ni Full'
    >>> analizar((6,4,1,5,3))
    'no se formo Generala,Poker ni Full'
    >>> analizar((6,4,2,3,3))
    'no se formo Generala,Poker ni Full'
    >>> analizar((4,4,4,4,4))
    'salio una Generala'
    >>> analizar((1,1,1,1,1))
    'salio una Generala'
    >>> analizar((1,1,2,1,1))
    'salio un Poker'
    >>> analizar((6,6,2,6,6))
    'salio un Poker'
    >>> analizar((5,3,5,3,3))
    'salio un Full'
    >>> analizar((2,2,4,2,4))
    'salio un Full'
    >>> analizar((1,5,1,5,1))
    'salio un Full'
    '''
    lista=[]
    lista=ingresa(tirada)
    lista=ordenar(lista)
    temp=lista[:]
    rolar=temp.pop(0)
    ocurre1=temp.count(rolar)
    if ocurre1 == 4:
        return 'salio una Generala'
    
    elif ocurre1 ==3:
        return 'salio un Poker'
    else:
        temp.insert(0,rolar)
        rolar=temp.pop()
        ocurre1=temp.count(rolar)
        if ocurre1 ==3:
             
            return 'salio un Poker'
    rolar=lista.pop(0)
    ocurre2=lista.count(rolar)
    if ocurre1+ocurre2==3:
        return 'salio un Full'
     
    return 'no se formo Generala,Poker ni Full'

print(analizar((6,5,2,3,4)))

import doctest
print(doctest.testmod())