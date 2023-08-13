'''
Escribir una función que reciba una cadena de caracteres que representa una dirección de mail.
La función debera devolver True ó False, en función de haber evaluado que dicha dirección está bien formada.
Se debe controla que:
 a. Que no contenga blancos
 b. Que sólo se utilicen letras y/o números para la parte del nombre, delante de la @
 c. Que haya exactamente una @
 d. Que los nombres de dominio sean: fi.uba.ar ó gmail.com
 e. Que tenga como máximo 30 caracteres

Para la solución no se podrán utilizar ciclos, y deberán aplicar los métodos existentes para cadenas tales como: count, index, isalnum, y cualquier otro que fuera necesario.

Probar la funcion mediante el uso de la libreria doctest, con los siguientes casos, y agregar nuevos casos para testear alternativas no contempladas en estos casos:

    >>> email_valido("jperez@fi.uba.ar")
    True
    >>> email_valido("j perez@fi.uba.ar")
    False
    >>> email_valido("j_perez@fi.uba.ar")
    False
    >>> email_valido("jperez@hotmail.com")
    False
    >>> email_valido("juanaugustolisandroperezgarciafernandez@fi.uba.ar")
    False
'''

def ingreso ():
    cadena=input("Ingrese una direccion de email: ")
    if verifBlancos(cadena):
        return 'La direccion ingresada contiene espacios en blanco'
    if verifLargo(cadena):
        return 'La direccion ingresada excede el maximo de 30 caracteres' 
    if verifArroba(cadena):
        return 'La direccion debe tener el simbolo @'
    if verifArrobas(cadena):
        return 'La direccion debe tener un solo simbolo @'
    

def verifBlancos(cadena):
    if cadena.count('')==0:
        return False
    return True

def verifLargo(cadena):
    if len(cadena)>30:
        return False
    return True

def verifArroba(cadena):
    if cadena.count('@')==0:
        return False
    return True

def verifArrobas(cadena):
    if cadena.count('@')>1:
        return False
    return True