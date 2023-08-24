'''
Se tiene una lista de un comercio donde se han registrado las unidades que se vendieron de cada producto en 
un día, como son ventas, los productos pueden aparecer más de una vez.

 productos = [ ['Agua', 10], ['Café', 2], ['Jugo', 3], ['Agua', 5], ['Mermelada', 1], ['Café', 1], ['Fideos', 5], ['Agua', 1], ['Fideos', 1] ]

a. Utilizando diccionarios calcular la cantidad que se vendió de cada producto. 

b. Ordenar los productos del más vendido al menos vendido
'''
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

def ordenDicc(diccio):
    lista=diccio.items()
    lista=sorted(lista,reverse=True, key=lambda item : item[1])
    diccio=dict(lista)
    return diccio

productos = [ ['Agua', 10], ['Café', 2], ['Jugo', 3], ['Agua', 5], ['Mermelada', 1], ['Café', 1], ['Fideos', 5], ['Agua', 1], ['Fideos', 1] ]
diccio=listaDicc(productos)
print(diccio)           #PUNTO A
diccio_orden=ordenDicc(diccio)
print(diccio_orden)     #PUNTO B
