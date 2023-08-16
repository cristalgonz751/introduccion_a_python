def de_a_dos (cadena):
    '''
    imprime cada 2 caracteres
    >>> de_a_dos('racimo')
    'rcm'
    >>> de_a_dos('herramienta')
    'hraina'
    '''
    return cadena[::2]

print(de_a_dos('viva la independencia'))
import doctest
print(doctest.testmod())