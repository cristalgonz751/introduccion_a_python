'''
Escribir un programa que permita al usuario crear una agenda de contactos. Para ello 
se debe tener en cuenta que: los nombres de los contactos no pueden estar repetidos 

a. crear una función “agregar contacto” que reciba una agenda (diccionario) un nombre 
y un teléfono, si el nombre del contacto ya existe en la agenda debe imprimir por pantalla 
“El usuario ya existe”, de lo contrario lo agrega el usuario a la agenda 

b. crear una función “actualizar contacto” que recibe una agenda (diccionario) un nombre 
y un teléfono, si el contacto existe en la agenda, actualiza su teléfono, sino debe 
imprimir por pantalla “El usuario no existe” 

c. crear una función “borrar contacto” que recibe una agenda y nombre de contacto y 
elimine el contacto
'''

def agregar_contacto(diccionario,nombre,telefono):
    mensaje=''
    lista=diccionario.items()
    posicion=0
    while lista[posicion][0]!=nombre and posicion!=len(lista):

    return mensaje