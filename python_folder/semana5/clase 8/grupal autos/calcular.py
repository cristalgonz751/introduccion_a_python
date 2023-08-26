'''
Ejercicio Grupal
1) Calcular el total de autos vendidos por cada vendedor utilizando un diccionario.
2) Calcular el importe total vendido por cada vendedor utilizando otro diccionario.
3) Hacer que los puntos anteriores esten ordenados de mayor a menor
'''

def crearDiccionarioVentasTotales(ventas):
  '''
  Recibe una lista de ventas:
  [ marca, modelo, int(cantidad vendida), vendedor, int(mes) ]

  Devuelve un diccionario:
  { vendedor: int( total vendido )}
  '''
  
  # Completar punto 1
  venta_ordenada=sorted(ventas,key=lambda item: item[3])
  datos = []
  
  for marca, modelo, cantidad, vendedor,mes in venta_ordenada:
    datos.append([vendedor,0])
    
  datos_ventas=dict(datos) 
  
  for clave in datos_ventas:
    cont = 0
    for marca, modelo, cantidad, vendedor,mes in venta_ordenada:
        if clave == vendedor:
            valor = cantidad
            cont += valor  
  
    datos_ventas[clave]=cont 
    datos_ventas[clave]=cont 
  
  return ordenarDiccionarios(datos_ventas)


def crearDiccionarioGananciasTotales(ventas, precios):
  '''
  Recibe una lista de ventas:
  [ marca, modelo, int(cantidad vendida), vendedor, int(mes) ]

  Recibe un diccionario de precios:
  { (marca, modelo): int(precio) }
  
  Devuelve un diccionario:
  { vendedor: int( total vendido )}
  '''
  
  # Completar punto 2
  venta_ordenada=sorted(ventas,key=lambda item: item[3])
  datos = []
  
  for marca, modelo, cantidad, vendedor,mes in venta_ordenada:
    datos.append([vendedor,0])
    
  datos_ventas=dict(datos)
  
  for clave in datos_ventas:
    cont = 0
    for marca, modelo, cantidad, vendedor,mes in venta_ordenada:
        if clave == vendedor:
            valor = cantidad
            auto = (marca,modelo)
            precio=precios[auto]
            cont += valor*precio  
  
    datos_ventas[clave]=cont 

  return ordenarDiccionarios(datos_ventas)

def ordenarDiccionarios(diccionario):
    datos_ordenados = diccionario.items()
    datos_ordenados = dict(sorted(datos_ordenados,key=lambda item : item[1],reverse=True))
    return datos_ordenados