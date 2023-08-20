'''
1. Calcular el promedio de notas de cada alumno y almacenarlos en una lista llamada
promedios.
2. Encontrar al alumno más joven y mostrar su información completa (nombre, edad y
notas).
3. Agregar una nueva columna a la tabla que indique si el alumno está "Aprobado" o
"Reprobado" en base a un promedio mínimo de 7.0.
4. Mostrar la tabla completa con la nueva columna agregada.
'''
NOMBRES=0
EDADES=1
NOTAS=2
FLOAT=0.1
INT=0
CADENA='A'

alumnos = [
["Ana", 18, [9, 8, 10]],
["Carlos", 17, [7, 6, 8]],
["María", 19, [10, 9, 9]],
["Luis", 18, [8, 7, 9]],
["Laura", 17, [6, 8, 7]]
]


promedios=[]
alumno=[]
datos=[]


def crearLista(lista,largo,tipo):
    for i in range(0,largo):
        lista[i]=tipo
    return lista

def promedio(datos,fila,promedios):
    promedios[fila]=sum(datos)/len(datos)
    return promedios

def buscar(alumnos,index):
    alumno=alumnos[index]
    return alumno

def lanzar(tabla,fila):
    dato=[]
    dato=tabla[fila]
    return dato,fila

promedios=crearLista(promedios,len(alumnos),FLOAT)

index=2
alumno=buscar(alumnos,index)

datos=lanzar(alumno,NOTAS)

promedios=promedio(datos,NOTAS,promedios)

print(promedios)

