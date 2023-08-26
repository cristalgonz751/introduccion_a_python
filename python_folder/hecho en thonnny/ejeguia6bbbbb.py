'''
5. Se tiene una tabla con información de alumnos. Cada fila representa a un alumno y
contiene su nombre, edad y notas en tres materias. Ordenar la lista por promedio en forma
descendente.
'''
alumnos = [
["Ana", 18, [9, 8, 10]],
["Carlos", 17, [7, 6, 8]],
["María", 19, [10, 9, 9]],
["Luis", 18, [8, 7, 9]],
["Laura", 17, [6, 8, 7]]
]

a=5
alumnes=alumnos.sort(reverse=True,key=lambda item: sum(item[2])/len(item[2]))
print(alumnos)
