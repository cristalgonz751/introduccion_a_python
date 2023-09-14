# abc='abcdefghijklmnopqrstuvwxyz'
# ABC=abc.upper()
# ABC=list(ABC)
# print(ABC)
# for i in range(0,7):
#     letra=ABC.pop(-1)
#     ABC.insert(0,letra)
# print(ABC)

def mensaje_alfa(cadena):
    alpha=True
    for letra in cadena:
        if letra.isalpha()==False and letra!=' ':
            alpha=False
    return alpha

def cesar(cadena,corrimiento):
    """
    funcion que encripta la cadena pasada por parametro con cifrado cesar
    y devuelve una cadena encriptada
    >>> cesar('ave cesarpo',corrimiento)
    'TOX VXLTKIH'
    >>> cesar('zzz zzz zzz',corrimiento)
    'SSS SSS SSS'
    >>> cesar('aaa AAA',corrimiento)
    'TTT TTT'
    >>> cesar('me apure demasiado rapido en la evaluacion',corrimiento)
    'FX TINKX WXFTLBTWH KTIBWH XG ET XOTENTVBHG'
    >>> cesar('por lo menos safe',corrimiento)  
    'IHK EH FXGHL LTYX'
    >>> cesar('los anos no vienen solos',corrimiento)   
    'EHL TGHL GH OBXGXG LHEHL'
    >>> cesar('mientras pueda certificar',corrimiento)
    'FBXGMKTL INXWT VXKMBYBVTK'
    >>> cesar('feo es mejor que lindo',corrimiento)
    'YXH XL FXCHK JNX EBGWH'
    >>> cesar('iesvs nazarenvs rex iudaervm',corrimiento)  
    'BXLOL GTSTKXGOL KXQ BNWTXKOF'
    >>> cesar('complicado es todo',corrimiento)
    'VHFIEBVTWH XL MHWH'
    >>> cesar('complicado es todo*',corrimiento)
    'ERROR el mensaje contiene caracteres no alfabeticos'
    """

    encriptado=[]
    cadena=cadena.upper()
    # print(cadena)
    if mensaje_alfa(cadena)==True:
        for letra in cadena:
            if letra==' ':
                encriptado.append(' ')
            
            elif corrimiento>=0:
                if ord(letra)+corrimiento<=90:
                    encriptado.append(chr(ord(letra)+corrimiento))
                else:
                    encriptado.append(chr(64+ord(letra)+corrimiento-90))

            else:
                if ord(letra)+corrimiento>=65:
                    encriptado.append(chr(ord(letra)+corrimiento))
                else:
                    encriptado.append(chr(91+ord(letra)+corrimiento-65))
        encriptado=''.join(encriptado)
    else: 
        encriptado='ERROR el mensaje contiene caracteres no alfabeticos'
    return encriptado

cadena='igni  naturae renovature integra'
corrimiento=-7
print(cesar(cadena,corrimiento))

import doctest
print(doctest.testmod())
