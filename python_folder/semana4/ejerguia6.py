materias=('matematica','ciencias naturales','historia','geografia','lengua')
notas = [
[8, 7, 10, 9, 9],
[7, 10, 8, 6, 7],
[9, 8, 10, 7, 8],
[6, 8, 7, 9, 10],
[10, 9, 7, 10, 8]
]

promedios = []
promediosmaterias=[]

def promedios(notas):
    promedios=[]
    for alumno in notas:
        promedio = sum(alumno)/len(alumno)
        promedios += [promedio]
    return promedios

def mostrar(notas,promedios):
    for im in range(0,len(notas)):
        print('nota de %s : %s'%(materias[im],notas[im]))
    print('promedio del alumno :%s'%promedios)
    return

def mayor(promedios):
    maximo=max(promedios)
    indice=promedios.index(maximo)
    return (indice)

def mayor_materia(notas):
    promediosmaterias=[]
    for ia in range(0,len(notas[0])):
        promedio=0
        for im in range(0,len(notas)):
            promedio+=notas[im][ia]
        promediosmaterias+=[promedio/len(notas[0])]
    return promediosmaterias
                    
    

promedios=promedios(notas)
for ia in range(0,len(notas)):
    mostrar(notas[ia],promedios[ia])
mejor_promedio=(mayor(promedios))
print('el alumno %s posee el mejor promedio'%(mejor_promedio+1))
mostrar(notas[mejor_promedio],promedios[mejor_promedio])
promediosmaterias=mayor_materia(notas)
print(promediosmaterias)

