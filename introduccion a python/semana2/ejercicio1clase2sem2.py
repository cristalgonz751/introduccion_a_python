def cada2(cadena):
    """
    imprime la cadena de a 2 caracteres
    >>> cada2('hola")
    'hl'
    >>> cada2('receta')
    'rct'
    """
    return cadena[::2]
cadena=input("ingresa una cadena:")
cada2(cadena)

import doctest
print(doctest.testmod())