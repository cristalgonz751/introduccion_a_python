def suma (num1,num2):
    '''
    funcion para sumar 2 numeros
    >>> suma(0,-2)
    -2
    >>> suma(2,-2)
    0
    '''

    return num1+num2
print(suma(2,6))

import doctest
print (doctest.testmod())

def suma2 (num1,num2,num3):
    '''
    funcion para sumar 2 numeros
    >>> suma2(0,-2,0)
    -2
    >>> suma2(2,-2,0)
    0
    '''

    return num1+num2+num3
print(suma2(-3,6,0))

#import doctest
print (doctest.testmod())
