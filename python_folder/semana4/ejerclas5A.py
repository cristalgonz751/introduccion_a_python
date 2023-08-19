notas=[]
contador=0
suma=0
minimo=10
maximo=1
while contador!=10:
    nota=input("ingrese nota:") 
    if nota.isnumeric()==True:
        nota=int(nota)
        if nota >=1 and nota <=10:
            notas.append(nota)
            contador+= 1
            suma+=nota
            if nota<minimo:
                minimo=nota
            elif nota>maximo:
                maximo=nota
        else:  
            print('NOTA NO VALIDA')      # PUNTO 2
    else:
        print('NO INGRESO UN NUMERO')    # PUNTO 2

promedio=suma/len(notas)
desvio_pos=maximo-(suma/len(notas))
desvio_neg=(suma/len(notas))-minimo
promocionados=[i for i in notas if 7<i<=10 ]
aprobados=[i for i in notas if 4<=i<=7 ]
reprobados=[i for i in notas if 1<=i<4 ]
print('notas: ',notas) #PUNTO 1
print('sumatoria de notas:',suma) # PUNTO 3
print('minima:',minimo) # PUNTO 3
print('maxima:',maximo) # PUNTO 3
print('promedio:',promedio) # PUNTO 4
print('max-prom:',desvio_pos) # PUNTO 5
print('prom-min:',desvio_neg) # PUNTO 5
print('la nota mas cerca al promedio es la', 'minima' if desvio_neg<desvio_pos else 'maxima') # PUNTO 6
#print('lista reprobados:',reprobados)
print('cantidad de reprobados:',len(reprobados)) # PUNTO 7
#print('lista de aprobados:',aprobados)
print('cantidad de aprobados:',len(aprobados)) # PUNTO 7
#print('lista promocionados:',promocionados)
print('cantidad de promocionados:',len(promocionados)) # PUNTO 7
promedio_high=sum(promocionados)/len(promocionados)
promedio_med=sum(aprobados)/len(aprobados)
promedio_down=sum(reprobados)/len(reprobados)
print('promedio de promocionados:',promedio_high) # PUNTO 8
print('promedio de aprobados:',promedio_med) # PUNTO 8
print('promedio de reprobados:',promedio_down) # PUNTO 8

