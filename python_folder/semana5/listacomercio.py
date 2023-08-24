'''
Se tiene una lista de un comercio donde se han registrado las unidades que se vendieron de cada producto en 
un día, como son ventas, los productos pueden aparecer más de una vez.

 productos = [ ['Agua', 10], ['Café', 2], ['Jugo', 3], ['Agua', 5], ['Mermelada', 1], ['Café', 1], ['Fideos', 5], ['Agua', 1], ['Fideos', 1] ]

a. Utilizando diccionarios calcular la cantidad que se vendió de cada producto. 

b. Ordenar los productos del más vendido al menos vendido
'''
def convertir(lista):
    diccionario=dict(lista)
    return diccionario

def ordenar(lista):
    lista_ordenada=sorted(lista, key=lambda item: item[0])
    return lista_ordenada

def ocurrencia(lista):
    lista_ocurrencia=[]
    acumulador=0
    for i in range(0,len(lista)):
        if i==len(lista)-1:
            tupla=()
            tupla=(lista[i][0],lista[i][1]+acumulador)
            lista_ocurrencia+=[tupla]
            return lista_ocurrencia
            
        elif lista[i][0]==lista[i+1][0]:
            acumulador=lista[i][1]+acumulador
        
        else:
            tupla=()
            tupla=(lista[i][0],lista[i][1]+acumulador)
            lista_ocurrencia+=[tupla]
            acumulador=0
    return lista_ocurrencia

def lisToDict(lista):
    lista=ordenar(lista)
    lista=ocurrencia(lista)
    dicc=convertir(lista)
    return(dicc)
diccio={}


def listaDicc(productos):
    listadicc=[]
    listaprod={}
    listaprod=dict(productos)

    for claves in listaprod:
        cont=0
        for item in productos:
            if item[0]== claves:
                cont+=item[1]
        listaprod[claves]=cont    
    return listaprod

productos = [ ['Agua', 10], ['Café', 2], ['Jugo', 3], ['Agua', 5], ['Mermelada', 1], ['Café', 1], ['Fideos', 5], ['Agua', 1], ['Fideos', 1], ['Mermelada', 1] ]
diccio=listaDicc(productos)
print(diccio)


ventas=lisToDict(productos)

print(ventas)
