"""
Escribir un programa que permita ingresar las notas de una cantidad indefinida de alumnos. 
A continuación el programa deberá mostrar: 

la cantidad de alumnos aplazados (nota menor a 4), 
la cantidad de alumnos aprobados (nota entre 4 y 7 inclusive) 
y la cantidad de alumnos que promocionan la materia (nota superior a 7). 
En cada caso, se mostrará el porcentaje del total de notas cargadas que cada caso representa.
Las notas son valores enteros y la carga finaliza cuando la nota ingresada es 0.
Ignorar las notas no válidas (fuera del rango de 1 a 10). 

Ejemplo: 

Ingrese nota: 5
Ingrese nota: 4 
Ingrese nota: 2 
Ingrese nota: 8
…
Ingrese nota: 0 

Cantidad de aplazos: 5 (10%) 
Cantidad de aprobados: 15 (30%) 
Cantidad de promocionados: 30 (60%)
"""
aplazados = 0
aprobados = 0
promocionados = 0
acu_notas = 0

def ingreso():
    nota=int(input("ingrese nota:"))
    if nota>0 and nota<11:
        condicion(nota)
        return True
    elif nota!=0:
        print("nota no valida")
        return True
    else:return False

def condicion(nota):
    global acu_notas
    acu_notas += 1
    if nota <4:
        global aplazados
        aplazados += 1
    elif nota>=4 and nota<=7:
        global aprobados
        aprobados += 1
    elif nota>7:
        global promocionados
        promocionados += 1 
    return

#print(aplazados,aprobados,promocionados,acu_notas)

while ingreso():
    ingreso()
print("Cantidad de aplazos",aplazados,"(",(aplazados/acu_notas*100),"%)")
print("Cantidad de aplazos",aprobados,"(",(aprobados/acu_notas*100),"%)")
print("Cantidad de aplazos",promocionados,"(",(promocionados/acu_notas*100),"%)")

