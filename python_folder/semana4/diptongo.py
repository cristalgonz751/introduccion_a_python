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
    '''
    for i in range(0,len(palabra)-1):
        if palabra[i] in 'iu':
            if palabra[i+1] in 'aeoáéóiuíú':
                return True
    
        elif palabra[i] in 'aeoáéó':
            if palabra[i+1] in 'iu':
                return True

    return False

print('destruí','tiene diptongo',diptongo('destruí') )
import doctest
print(doctest.testmod())