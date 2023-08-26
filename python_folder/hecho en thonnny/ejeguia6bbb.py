'''
1. Calcular el promedio de kilometraje de los autos y almacenarlo en una variable
llamada promedioKilometraje.
2. Encontrar el auto más antiguo y mostrar su información completa (marca, modelo,
año y kilometraje).
3. Agregar una nueva columna a la tabla que indique si el auto es "Nuevo" (menos de 2
años de antigüedad) o "Usado".
4. Mostrar la tabla completa con la nueva columna agregada.
'''
FLOAT=0.1
INT=0
CADENA='A'
MARCA=0
MODELO=1
YEARS=2
KM=3
ACTUAL=2023

autos = [
["Toyota", "Corolla", 2022, 25000],
["Ford", "Focus", 2018, 38000],
["Honda", "Civic", 2019, 32000],
["Chevrolet", "Cruze", 2020, 27000],
["Nissan", "Sentra", 2017, 42000]
]

tabla=autos

promedios=[]
years=[]
auto=[]
datos=[]

def crearLista(lista,largo,tipo):
    for i in range(0,largo):
        lista.append(tipo)
    return lista

def buscar(tabla,index):
    fila=tabla[index]
    return fila

def lanzar(tabla,columna,fila):
    dato=[]
    dato=tabla[columna]
    return dato,fila

def promedio(datos,promedios):
    promedios[datos[1]]=datos[0]/len(tabla)
    return promedios

def	menor(tabla):
    tabla.sort(key=lambda item: item[2])
    return tabla[0]

def agregartabla(datos,lista):
    newold=[]
    if ACTUAL-datos[0]<2:
        newold.append('NUEVO')
    else:
        newold.append('USADO')
    lista[datos[1]].append(newold)
    return lista

def punto(lista,fila,datos,columna,funcion):
    for index in range(0,len(tabla)):
        fila=buscar(tabla,index)
        datos=lanzar(fila,columna,index)
        lista=funcion(datos,lista)
    return lista

promedios=crearLista(promedios,len(tabla),FLOAT)
funcion=promedio
promedios=punto(promedios,auto,datos,KM,funcion)
promedioKilometraje=sum(promedios)                              #PUNTO 1

antiguo=menor(tabla)

funcion=agregartabla
autos=punto(autos,auto,datos,YEARS,funcion)

print(promedioKilometraje)
print('el auto mas antiguo es un %s modelo %s del %s con %s Km'%(antiguo[0],antiguo[1],antiguo[2],antiguo[3]))
for auto in autos:
    print(auto)
