'''
Ahora vamos a escribir un programa que simule una situación de juego,
 utilizando las funciones escritas en los puntos anteriores;
y sumando nuevas funciones para lo que se solicite en este punto específicamente.

Escribir un programa que genere 1000 tiradas aleatorias, de los 5 dados.
Por cada tirada, se debe clasificar si corresponde a alguna de las categorías
 para las que hemos escrito las funciones (Escalera, Generala, Póker, Full), ó a ninguna.

El programa deberá emitir un informe que indique
La cantidad de tiradas coincidentes con cada categoría 
(incluída que no coincide con ninguna categoría), 
El % que representa cada una. 
Ayuda adicional
Para la generación de cada tirada aleatoria, será necesario hacer uso del 
método choices(), del módulo random.
Para ello es necesario que:
  a. Importes el módulo mediante el uso de la siguiente línea: import random
  b. Para generar cada una de las listas de los 6 elementos aleatorios debes usar:
   random.choices([1,2,3,4,5,6], k=5)

'''

def	ordenar(lista):
    lista.sort()
    return lista

def analizar(tirada):
    '''
    analiza la jugada de 5 dados
    '''
    lista=[]
    lista=tirada
    lista=ordenar(lista)
    temp=lista[:]
    if lista == [1,2,3,4,5]:
        return 0 #        print('salio la escalera [1,2,3,4,5]')
    elif lista == [2,3,4,5,6]:
        return 0 #        print('salio la escalera [2,3,4,5,6]')
    rolar=lista.pop(0)
    lista.append(rolar)
    if lista == [3,4,5,6,1]:
        return 0 #        print('salio la escalera [3,4,5,6,1]')

    rolar=temp.pop(0)
    ocurre1=temp.count(rolar)
    if ocurre1 == 4:
        return 1 #'salio una Generala'
    
    elif ocurre1 ==3:
        return 2 #'salio un Poker'
    else:
        temp.insert(0,rolar)
        rolar=temp.pop()
        ocurre1=temp.count(rolar)
        if ocurre1 ==3:
             
            return 2 #'salio un Poker'
    rolar=lista.pop(0)
    ocurre2=lista.count(rolar)
    if ocurre1+ocurre2==3:
        return 3 #'salio un Full'
     
    return 5 #'no se formo Generala,Poker ni Full'

import random

def generar():
    jugada=[]
    jugada=random.choices([1,2,3,4,5,6], k=5)
    return jugada

def simulacion():
    contadores=[0,0,0,0,0]
    for i in range(0,1000):
        resultado=analizar(generar())
        if resultado==0:
            contadores[0]+=1
        elif resultado==1:
            contadores[1]+=1
        elif resultado==2:
            contadores[2]+=1
        elif resultado==3:
            contadores[3]+=1
        else:
            contadores[4]+=1
    porcentaje=[]
    porcentaje=[(x/1000)*100 for x in contadores ]
    print('escalera:%s jugadas representa un porcentaje de %s'%(contadores[0],porcentaje[0]))
    print('generala:%s jugadas representa un porcentaje de %s'%(contadores[1],porcentaje[1]))
    print('poker:%s jugadas representa un porcentaje de %s'%(contadores[2],porcentaje[2])) 
    print('full:%s jugadas representa un porcentaje de %s'%(contadores[3],porcentaje[3]))
    print('no exitosa:%s jugadas representa un porcentaje de %s'%(contadores[4],porcentaje[4]))
    return 

simulacion()

