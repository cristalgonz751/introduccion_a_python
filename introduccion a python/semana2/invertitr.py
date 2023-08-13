import doctest

def invertir(cadena):
    """
    >>> invertir('hola mundo')
    'odnum aloh'
    >>> invertir('123')
    '321'
    """
    return cadena[::-1]

print(invertir('hola'))

print (doctest.testmod())