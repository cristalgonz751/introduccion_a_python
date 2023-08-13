"""
Escribir un programa que simule el proceso de control de peso y cantidad de personas que puede transportar un 
ascensor.
Vamos a suponer que nuestro ascensor puede soportar un máximo de 400 kg y hasta 6 personas.

Nuestra simulación debe proceder del siguiente modo:
A medida que las personas ingresan al ascensor de a una a la vez, se registra el peso de la persona.
Supondremos que el ingreso de 0 kg, indica que no hay más personas por subir al ascensor.
Si en un determinado momento del ingreso de las personas, se supera el peso máximo,
el ascensor, advertirá mediante un mensaje, que indique que se ha excedido el peso máximo y nuestra simulación 
terminará.
De igual modo, si el ascensor detecta que ha subido una séptima persona al ascensor, deberá advertir de esto, y 
nuestra simulación terminará.
Por último, si habiéndose indicado que todas las personas están abordo del ascensor y las condiciones
 establecidas se cumplen, el ascensor anunciará "ascensor en movimiento".
"""

import doctest
def evaluar (peso,persona,pesoTotal):
    '''
    utilice una funcion ya que se podria pasar tambien un max o cantidad 
    como parametro y reutilizar la funcion
    >>> evaluar(100,5,400)
    ('el acensor esta exedido de peso :500 kg', 0, 5, 500)
    >>> evaluar(100,5,300)
    ('evaluando', 100, 6, 400)
    '''     
    if peso == 0:
        return 'el acensor esta en movimiento con %s personas y un peso de %s kg' %(persona,pesoTotal), 0,persona,pesoTotal
    pesoTotal += peso
    if pesoTotal<=400:
        persona +=1
        if persona == 7:
            return 'el acensor esta exedido en cantidad, hay %s personas' %persona, 0,persona,pesoTotal
    else:
        return 'el acensor esta exedido de peso :%s kg' %pesoTotal, 0,persona,pesoTotal
    #print(pesoTotal)
    return 'evaluando',peso,persona,pesoTotal

def validar(peso):                  
    '''
    para validar que sea un numero positivo o nulo 
    >>> validar('-10')
    False
    >>> validar('0')
    True
    >>> validar('O')
    False
    '''
    if peso.isnumeric() and int(peso)>=0:
        return True
    return False

resultado,peso="",1
persona=0


while peso !=0 :
    if persona == 0:
        pesoTotal=0
    peso=input('Ingrese el peso de la persona en kg o 0 para terminar:')
    if validar(peso):
        peso=int(peso)
        resultado,peso,persona,pesoTotal = evaluar(peso,persona,pesoTotal)
    else:
        print('ENTRADA INVALIDA')



print(resultado)

print(doctest.testmod())



