def invertir(cadena):
    """
    >>> invertir('hola mundo')
    'odnum aloh'
    >>> invertir('123')
    '321'
    """
    return cadena[::-1]

print('reflejo'+invertir('reflejo'))
import doctest
print (doctest.testmod())