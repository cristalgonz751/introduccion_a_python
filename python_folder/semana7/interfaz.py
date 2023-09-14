
from cifrado_cesar import cesar
from cifrado_atbash import atbash

def menu(pregunta,opcion1,opcion2):
    print('     %s         %s         %s'%(pregunta,opcion1,opcion2))               
    return   (input('         '))

def ingresar(opcion):
    if opcion=='1':
        mensaje=menu('Ingrese el mensaje que desea cifrar:','','')
    else:
        mensaje=menu('Ingrese el mensaje que desea descifrar:','','')
    return mensaje

def metodo_ejecutar():
    metodo=menu('Que cifrador desea usar:\n','1)Cesar\n','2)Atbash')
    return metodo

    
def ejecutar(mensaje,opcion,metodo):
    if metodo=='1':
        clave=menu('Que clave desea utilizar para el cifrado Cesar:','','')
        if opcion=='1':
            resultado=cesar(mensaje,int(clave))
        else:
            resultado=cesar(mensaje,int(clave)*-1)


    else:
        resultado=atbash(mensaje)
    
    return resultado
#ERWHOOD
def enviar_mensaje(resultado):
    return

def informar(resultado,opcion):
    if opcion=='1':
        print('     Su mensaje cifrado es:',resultado)
    else:
        print('     Su mensaje descifrado es:',resultado)

opcion=menu('Que desea hacer:\n','1) Cifrar mensaje\n','2) Descifrar mensaje')
mensaje=ingresar(opcion)
metodo=metodo_ejecutar()
resultado=ejecutar(mensaje,opcion,metodo)
enviar_mensaje(resultado,opcion)
informar(resultado,opcion)
