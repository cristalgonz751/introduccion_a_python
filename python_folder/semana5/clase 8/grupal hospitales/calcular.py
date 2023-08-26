
'''
Guía de ejercicios del material de la cátedra:

6. Escribir un programa, compuesto por funciones, que permita:

a) Ingresar en un diccionario, localidades (como clave) y dos datos: cantidad de
 habitantes y cantidad de hospitales públicos (HP). Los datos surgen de distintas
   planillas, por lo que una misma clave (localidad) se puede ingresar varias veces,
     debiendo sumarse los valores.

b) Listar el total de habitantes y HP para cada localidad.

c) Imprimir un listado ordenado de mayor a menor de las 5 localidades de mayor relación:
 (habitantes / HP). Indicar la Localidad y la relación resultante.
'''

def crearDiccionarioHyHxLocalidad(planillas):
    relevamiento={}
    for planilla in planillas:
        for localidad,habitantes,hospitales in planilla:
            if localidad not in relevamiento:
                relevamiento[localidad]=[habitantes,hospitales]

            else:
                relevamiento[localidad][0]+=habitantes
                relevamiento[localidad][1]+=hospitales
 

    return relevamiento

def crearDiccionarioIndice(datosPorLocalidad):
    relevamientoIndice=[]
    datosPorLocal=datosPorLocalidad.items()
    for localidad,datos in  datosPorLocal:
        relevamientoIndice.append([localidad,datos[0]/datos[1]])
    relevamientoIndice.sort(key=lambda item: item[1],reverse=True)
    relevamientoIndice=relevamientoIndice[:5]
    relevamientoIndice=dict(relevamientoIndice)
    return relevamientoIndice