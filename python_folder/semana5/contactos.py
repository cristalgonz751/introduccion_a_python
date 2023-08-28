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

def agregar_contacto(agenda,nombre,telefono):
    if nombre not in agenda:
        agenda[nombre]=telefono
    else: print('El usuario no existe')
    return 

def actualizar_contacto(agenda,nombre,telefono):
    if nombre in agenda:
        agenda[nombre]=telefono
    else:
        print('El usuario no existe') 
    return 

def borrar_contacto(agenda,nombre):
    if nombre in agenda:
        del(agenda[nombre])
    else:
        print('El usuario no existe')     
    return 


def ingresar_datos(agre_act):
    nombre=input('ingrese el nombre:')
    if agre_act == True:
        telefono=input('ingrese un numero de télefono:')
        return nombre,telefono
    return nombre
    

def mostrar_contactos(agenda):
    for contacto in agenda:
        print(contacto.ljust(20) ,'|', agenda[contacto].ljust(20) )

def interfaz_agenda():
    agenda={}
    opcion=0
    while opcion!=5:
        print('\n 1) Crear contacto \n 2) Actualizar contacto \n 3) Borrar contacto \n 4) Mostrar Contactos \n 5) Salir ')
        opcion=int(input('Ingrese la opción :'))
        if opcion==1:
            (nombre,telefono)=ingresar_datos(True)
            agregar_contacto(agenda,nombre,telefono)
        elif opcion==2:
            nombre,telefono=ingresar_datos(True)
            actualizar_contacto(agenda,nombre,telefono)
        elif opcion==3:
            nombre=ingresar_datos(False)
            borrar_contacto(agenda,nombre)
        elif opcion==4:
            mostrar_contactos(agenda)
            
    return

interfaz_agenda()
