'''
Escribir una función que reciba una cadena de caracteres.
La función deberá evaluar si la cadena recibida representa un número binario, y en ese caso devolver True, de lo contrario, deberá devolver False.
No se pueden utilizar ninguno de los métodos tales como isnumeric, isalpha, isalnum.
Se debe evitar la realización de ciclos innecesario, mediante la aplicación del ciclo correcto.

Probar la funcion mediante el uso de la libreria doctest, con los siguientes casos:

'''

def binario(cadena):
    '''
    la funcion devuelve True si la cadena es un numero binario
    >>> binario("0A101010111111111011111011111110")
    False
    >>> binario("011101")
    True
    >>> binario("")
    False
    >>> binario("1")
    True
    >>> binario("0")
    True
    '''
    if cadena == '':
        return False
    for posicion in cadena:
        if posicion not in '01' :
            return False
    return True

print(binario('0111x11'))
print(binario('%$'))
print(binario('0'))

import doctest
print(doctest.testmod())