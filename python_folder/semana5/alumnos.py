'''
Se tiene una tabla con información de alumnos. Cada fila representa a un alumno y contiene su nombre,
 edad y notas en tres materias.

alumnos = [ ["Ana", 18, [9, 8, 10]], ["Carlos", 17, [7, 6, 8]], ["María", 19, [10, 9, 9]], ["Luis", 18, [8, 7, 9]], ["Laura", 17, [6, 8, 7]] ]

a. Escribir una función que transforme la lista anterior a un diccionario donde la clave sea el nombre 
del alumno:
dictAlumnos = { "Ana" : [8, [9, 8, 10]], "Carlos": [ 17, [7, 6, 8]], "María": [ 19, [10, 9, 9]], "Luis": [ 18, [8, 7, 9]], "Laura": [ 17, [6, 8, 7]] }
b. Escribir una función que calcule el promedio de notas de cada alumno y lo agregue al diccionario
 anterior.
c. Escribir una función que encuentre al alumno con menor promedio y devuelva sus datos.
'''
diccio={}

def listaDicc(alumnos):
    diccio={}
    for alumno in alumnos:
        diccio[alumno[0]]=[alumno[1],alumno[2]]
    return diccio

def listaDiccExt(alumnos):
    diccio={}
    for alumno in alumnos:
        diccio[alumno[0]]=[alumno[1],alumno[2],alumno[3]]
    return diccio

def promedio(alumnos):
    for alumno in alumnos:
        promedio=sum(alumno[2])/len(alumno[2])
        alumno.append(promedio)
    return alumnos

def ordenar(alumnos):
    alumnosort=sorted(alumnos, reverse=False,key=lambda item: item[3])
    return alumnosort


alumnos = [ ["Ana", 18, [9, 8, 10]], ["Carlos", 17, [7, 6, 8]], ["María", 19, [10, 9, 9]], ["Luis", 18, [8, 7, 9]], ["Laura", 17, [6, 8, 7]] ]

diccio=listaDicc(alumnos)       #PUNTO A
print(diccio)
alumnosext=promedio(alumnos)
diccio=listaDiccExt(alumnosext) #PUNTO B
print(diccio)
alumnomin=ordenar(alumnosext)
print(alumnomin[0])             #PUNTO C
