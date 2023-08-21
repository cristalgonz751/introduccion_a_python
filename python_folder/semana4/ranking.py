'''
Escribir una función que reciba un texto y devuelva una lista anidada que representa un ranking de palabras.
El texto puede tener gran cantidad de palabras.

La función deberá devolver una lista anidada, en la que cada sublista, esté formada por un par [palabra, cantidad de veces en el texto].

Las palabras sólo deben aparecer una vez en la lista.

Ejemplo
>>> ranking( "no se como como como no se cayó" )
[ ["como ", 3], ["no", 2] , ["se", 2], ["cayó", 1]  ]
'''



def hacer_lista(texto):
    lista=texto.split(separador)
    return lista

def ordenar(lista):
    lista_ordenada=[]
    lista_ordenada=sorted(lista)
    return lista_ordenada

def ocurrencias(ordenada):
    repetidas=[]
    contar=1
    while ordenada!=[]:       
        palabra=ordenada.pop(0)
        if palabra in ordenada and contar<max_ocurren:
            contar+=1
        else:
            repetidas.append((palabra,contar))
            contar=1
    return repetidas
    

texto='esta#oracion#debe#ser#un#poco#larga#esta#vez#debe#ser#asi#un#poco#sin#sentido#la#oracion#debe#ser#asi#nomas'

separador='#'				#el tipo de separador para el split
max_ocurren=2				#pasarle el maximo de ocurrencias


def ranking(texto,separador,max_ocurren):
    lista=[]
    ordenada=[]
    ocurren=[]
    lista=hacer_lista(texto)
    ordenada=ordenar(lista)
    ocurren=ocurrencias(ordenada)
    ocurren.sort(reverse=True,key=lambda item: item[1])
    return	ocurren

print(ranking(texto,separador,max_ocurren))

