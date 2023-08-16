def diasMes (mes,año):
    '''
    funcion que devuelve los dias del mes segun el año
    >>> diasMes(12,1987)
    31
    >>> diasMes(5,1782)
    31
    >>> diasMes(2,2023)
    28
    >>> diasMes(2,1912)
    29
    >>> diasMes(2,1988)
    29
    >>> diasMes(2,1700)
    28
    >>> diasMes(2,1600)
    29
    >>> diasMes(2,1900)
    28
    >>> diasMes(2,2200)
    28
    >>> diasMes(2,2000)
    29
    '''
    if mes==1:  
        return 31
    if mes==2:
        if (biciesto(año)):
            return 29
        else: return 28
    if mes==3:
        return 31
    if mes==4:
        return 30
    if mes==5:
        return 31
    if mes==6:
        return 30
    if mes==7:
        return 31
    if mes==8:
        return 31
    if mes==9:
        return 30
    if mes==10:
        return 31
    if mes==11:
        return 30
    if mes==12:
        return 31
           
def biciesto(año):
    if año % 4 == 0 and año % 100 ==0 and año % 400 !=0:
        return False
    elif año % 4==0:
        return True
    else:return False

import doctest
print (doctest.testmod())

print(diasMes(2,2100))    



