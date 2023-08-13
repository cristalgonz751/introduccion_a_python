def multiplicar_positivos(a,b):
    """
    >>> multiplicar_positivos(5,10)
    50
    """
    val_minino = min(a,b)
    val_maximo = max(a,b)
    suma=0
    for i in range(val_minino):
        suma += val_maximo
    return suma

def signo_multiplicacion(a,b):
    signo = 1
    if a<0 and b>0:
        signo = -1
    elif b<0 and a>0:
        signo = -1
    return signo

def multiplicacion(a,b):
    """
    >>> multiplicacion(3,3)
    9
    >>> multiplicacion(-3,-3)
    9
    >>> multiplicacion(-3,3)
    -9
    >>> multiplicacion(3,-3)
    -9
    >>> multiplicacion(-100,3)
    -300
    """
    signo = signo_multiplicacion(a,b)
    valor = multiplicar_positivos( abs(a), abs(b) )
    return signo*valor

import doctest
print( doctest.testmod() )
print(multiplicacion(-100,3))
