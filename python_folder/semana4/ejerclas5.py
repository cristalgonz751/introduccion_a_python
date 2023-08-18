notas=[]
contador=0
suma=0
minimo=10
maximo=1
while contador!=10:
    nota=int(input("ingrese nota:"))
    if nota >=1 and nota <=10:
        notas.append(nota)
        contador+= 1
        suma+=nota
        if nota<minimo:
            minimo=nota
        elif nota>maximo:
            maximo=nota

promocionados=[i for i in notas if 7<i<=10 ]
aprobados=[i for i in notas if 4<=i<=7 ]
reprobados=[i for i in notas if 1<=i>4 ]

print('sumatoria de notas:',suma)
print('minima:',minimo)
print('maxima:',maximo)
print('promedio:',suma/len(notas))
print('max-prom:',maximo-(suma/len(notas)))
print('prom-min:',(suma/len(notas))-minimo)
print('lista aprobados:',aprobados)
print('cantidad de aprobados:',len(aprobados))
print('mi')

