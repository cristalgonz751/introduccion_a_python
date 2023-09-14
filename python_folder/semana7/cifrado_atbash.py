
from cifrado_cesar import mensaje_alfa

def atbash(cadena):
    '''
    funcion se le pasa cadena por argumento y devuelve la cadena codificada en atbash
    >>> atbash('A')
    'Z'
    >>> atbash('Z')
    'A'
    >>> atbash('ABBA')
    'ZYYZ'
    >>> atbash('ABBA')
    'ZYYZ'
    >>> atbash('ZYXWVUTSRQPONMLKJIHGFEDCBA')
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> atbash('ZYXWVUTSRQPONMLKJIHGFEDCBAabcdefghijklmnopqrstuvwxyz')
    'ABCDEFGHIJKLMNOPQRSTUVWXYZZYXWVUTSRQPONMLKJIHGFEDCBA'
    >>> atbash('ABCDEFGHIJKLMNOPQRSTUVWXYZZYXWVUTSRQPONMLKJIHGFEDCBA')
    'ZYXWVUTSRQPONMLKJIHGFEDCBAABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> atbash('atbash')
    'ZGYZHS'
    >>> atbash('menem lo hizo')
    'NVMVN OL SRAL'
    >>> atbash('carnes asadas convido al pueblo')
    'XZIMVH ZHZWZH XLMERWL ZO KFVYOL'
    '''
    cadena=cadena.upper()
    if mensaje_alfa(cadena)==True:
        atbash=[]
        for letra in cadena:
            if letra==' ':
                atbash.append(' ')
            else:    
                atbash.append(chr(90-(ord(letra)-65)))
        atbash=''.join(atbash)
        return atbash
    else:
        atbash='ERROR el mensaje contiene caracteres no alfabeticos'
cadena='quien dio su voto creyendo*'
print(atbash(cadena))

import doctest
print(doctest.testmod())