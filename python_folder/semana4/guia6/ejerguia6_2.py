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
NOTAPROBADO=7

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
        lista.append(tipo)
    return lista

def promedio(datos,promedios):
    promedios[datos[1]]=sum(datos[0])/len(datos[0])
    return promedios

def agregartabla(datos,lista):
    aprorepro=[]
    for nota in datos[0]:
        if nota>=7:
            aprorepro.append('Aprobado')
        else:
            aprorepro.append('Reprobado')
    lista[datos[1]].append(aprorepro)
    return lista


def edad(datos,edades):
    edades[datos[1]]=datos[0]
    return edades

def buscar(alumnos,index):
    alumno=alumnos[index]
    return alumno

def lanzar(tabla,columna,fila):
    dato=[]
    dato=tabla[columna]
    return dato,fila

promedios=crearLista(promedios,len(alumnos),FLOAT)

def punto(lista,alumno,datos,columna,funcion):
    for index in range(0,len(alumnos)):
        alumno=buscar(alumnos,index)
        datos=lanzar(alumno,columna,index)
        lista=funcion(datos,lista)
    return lista

def menor(tabla):
    tabla.sort(key=lambda item: item[1])
    return tabla[0]



funcion=promedio
promedios=punto(promedios,alumno,datos,NOTAS,funcion)					#PUNTO 1


tabla=alumnos							                                #PUNTO 2
alumnoMenor=menor(tabla)
print('El alumno %s su edad es %s sus notas son \n Matematica: %s \n Lengua: %s \n Geografia: %s' %(alumnoMenor[0],alumnoMenor[1],alumnoMenor[2][0],alumnoMenor[2][1],alumnoMenor[2][2]))

funcion=agregartabla
alumnos=punto(alumnos,alumno,datos,NOTAS,funcion)						#PUNTO 3

    
for alumno in alumnos:													#PUNTO 4
    print(alumno)