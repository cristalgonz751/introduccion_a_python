'''

Escribir una función que reciba una palabra, y devuelva True, si la palabra tiene diptongo, y False,
en caso contrario. Asumir que la palabra recibida, solo esta formada por letras. En español dos
vocales en contacto se articulan como diptongo cuando: 1) una es cerrada (i u) átona (no acentuada) y
la otra es abierta (a e o) y viceversa. 2) ambas son cerradas, excepto si son iguales (como en chiita),
donde forman un hiato.
'''

def diptongo(palabra):
    '''
    funcion que devuelve true si la cadena que pasamos
    por valor tiene diptongo
    >>> diptongo('náutico')
    True
    >>> diptongo('adiós')
    True
    >>> diptongo('después')
    True
    >>> diptongo('acuífero')
    True
    >>> diptongo('hiato')
    True
    >>> diptongo('día')
    False
    >>> diptongo('chiita')
    False
    >>> diptongo('quiebra')
    True
    >>> diptongo('quiero')
    True
    >>> diptongo('opioide')
    False
    >>> diptongo('estudiáis')
    False
    >>> diptongo('paraguay')
    False
    >>> diptongo('diptongo')
    False
    '''
    # for i in range(0,len(palabra)-1):
    #     if palabra[i] in 'iu':
    #         if palabra[i+1] in 'aeoáéóiuíú':
    #             if palabra[i]!=palabra[i+1]:        #que no sea hiato
    #                 if palabra[i+2] not in 'iuy':   #que no sea triptongo
    #                     return True

    
    for i in range(0,len(palabra)-1):
        if palabra[i] in 'iu' and palabra[i+1] in 'aeoáéóiuíú' and palabra[i]!=palabra[i+1]:
            if i+2<=len(palabra) and palabra[i+2] in 'iuy':
                return False
            return True
        
        elif palabra[i] in 'aeoáéó' and palabra[i+1] in 'iu':           
                return True
    
        # elif palabra[i] in 'aeoáéó':
        #     if palabra[i+1] in 'iu':
        #         return True

    return False

print('destruí','tiene diptongo',diptongo('destruiste') )
import doctest
print(doctest.testmod())