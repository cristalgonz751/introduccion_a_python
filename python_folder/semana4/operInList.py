lista=[]
ocurrencia=3
print('Ingresar valores para terminar ingrese 0')

def ingreso(lista):
    valor=1
    while valor != 0:
        valor=int(input('Ingrese un valor:'))
        if valor != 0:
            lista += [valor] 
    return lista

lista=ingreso(lista)                 #PUNTO 1


def paridad(valor):
    resultado = True if valor % 2 != 0 else False
    return resultado

def recorrer(lista,ocurrencias):
    lista_impar = []
    posicion = 0
    while ocurrencias != 0 and posicion < len(lista):
        if paridad(lista[posicion])==True:
            lista_impar += [lista[posicion]]
            ocurrencias -= 1
        posicion += 1
    return lista_impar

def pos_par(lista):
    return lista[::2]

def lista_no_repit(lista):
    lista_no_repit=[]
    for valor in lista:
        if valor not in lista_no_repit:
            lista_no_repit += [valor]
    return lista_no_repit

def mostrar(mensaje,lista):
    print(mensaje)
    for i in range(0,len(lista)) :
        print('posicion %s valor: %s'%(i,lista[i]))

    return


mostrar('lista ingresada',lista)                                                                #PUNTO 1
mostrar('lista de los primeros 3 elementos impares si los hay',recorrer(lista,ocurrencia))      #PUNTO 2
mostrar('lista de elementos en posiciones pares',pos_par(lista))                                #PUNTO 3
lista_no_repit=lista_no_repit(lista)
lista_no_repit.sort()
mostrar('lista ordenada de elementos sin repeticion',lista_no_repit)                            #PUNTO 4

