'''Escribir una función que reciba una cadena de caracteres y devuelva  una cadena, formada por las vocales que se encuentran en la cadena recibida.
Respetar el orden de aparición.
Probar la funcion mediante el uso de la libreria doctest, con los siguientes casos:


Escribir una función que reciba una cadena de caracteres y devuelva  una cadena, formada por las consonantes que se encuentran en la cadena recibida.
Respetar el orden de aparición.
Probar la funcion mediante el uso de la libreria doctest, con los siguientes casos:
'''


def consonantes(cadena):
    '''
    la funcion devuelve una cadena que contiene solo las consonantes
    de la cadena cadena valga la redundancia
    >>> consonantes("campana")
    'cmpn'
    >>> consonantes("pueblo")
    'pbl'
    >>> consonantes("cg9")
    'cg'
    >>> consonantes('gato') 
    'gt'
    >>> consonantes('gafa')
    'gf'
    '''
    resultado = ''
    for letra in cadena:
        if letra not in 'aeiouAEIOU' and letra.isalpha():
            resultado += letra
    return resultado

print(consonantes('campana'))
print(consonantes('pueblo'))
print(consonantes('cg9'))

import doctest
print(doctest.testmod())
