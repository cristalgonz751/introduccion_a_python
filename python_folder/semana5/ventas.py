'''
Se tiene la misma lista de ventas de productos del ejercicio 1, pero ahora además tenemos 
otra lista donde se tienen los precios de cada producto:
productos = [ ['Agua', 10], ['Café', 2], ['Jugo', 3], ['Agua', 5], ['Mermelada', 1], ['Café', 1], ['Fideos', 5], ['Agua', 1], ['Fideos', 1]]
precios = [ ['Mermelada', 500], ['Agua', 100], ['Fideos', 350], ['Jugo', 50], ['Cafe', 600], ]
Escribir una función que reciba ambas listas por parámetro y devuelva un diccionario que 
tenga como claves, los nombres de los productos y como valor, una lista que contenga la 
cantidad de unidades vendidas, el precio unitario, y el precio total 
(precio unitario * cantidades vendidas). Es decir:
reporte = { 'Fideos': [6, 350, 2100], 'Café': [3, 600, 1800], 'Agua': [16, 100, 1600], 'Mermelada': [1, 500, 500], 'Jugo': [3, 50, 150] }
'''
''
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

# productos = [ ['Agua', 10], ['Café', 2], ['Jugo', 3], ['Agua', 5], ['Mermelada', 1], ['Café', 1], ['Fideos', 5], ['Agua', 1], ['Fideos', 1] ]

# print(diccio)           #PUNTO A
# diccio_orden=ordenDicc(diccio)
# print(diccio_orden)     #PUNTO B


def pegatablas(productos,precios):
    diccio=listaDicc(productos)
    for clave in diccio:
        for precio in precios:
            if clave==precio[0]:
                datos=[]
                valor=diccio[clave]
                datos=[valor,precio[1],valor*precio[1]]
                diccio[clave]=datos
    return diccio



productos = [ ['Agua', 10], ['Café', 2], ['Jugo', 3], ['Agua', 5], ['Mermelada', 1], ['Café', 1], ['Fideos', 5], ['Agua', 1], ['Fideos', 1]]
precios = [ ['Mermelada', 500], ['Agua', 100], ['Fideos', 350], ['Jugo', 50], ['Café', 600], ]




reporte=pegatablas(productos,precios)
print(reporte)