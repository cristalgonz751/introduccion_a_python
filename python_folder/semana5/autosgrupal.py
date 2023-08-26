'''
Ejercicio Grupal
1) Calcular el total de autos vendidos por cada vendedor utilizando un diccionario.
2) Calcular el importe total vendido por cada vendedor utilizando otro diccionario.
3) Hacer que los puntos anteriores esten ordenados de mayor a menor
'''
ventas = [['Toyota', 'Corolla', 10, 'Juan Pérez', 12],
          ['Honda', 'Civic', 5, 'Laura Sánchez', 11],
          ['Ford', 'Mustang', 3, 'María Gómez', 11],
          ['Chevrolet', 'Cruze', 8, 'Pedro González', 12],
          ['Honda', 'Golf', 1, 'Carlos López', 11],
          ['Toyota', 'Corolla', 6, 'Pedro González', 11],
          ['Honda', 'Civic', 7, 'Carlos López', 12],
          ['Ford', 'Mustang', 4, 'Pedro González', 12],
          ['Chevrolet', 'Cruze', 2, 'Laura Sánchez', 12],
          ['Honda', 'Golf', 12, 'María Gómez', 11],
          ['Toyota', 'Corolla', 15, 'Juan Pérez', 11],
          ['Honda', 'Civic', 13, 'Juan Pérez', 11],
          ['Ford', 'Mustang', 12, 'María Gómez', 12],
          ['Chevrolet', 'Cruze', 7, 'Pedro González', 11],
          ['Honda', 'Golf', 10, 'Carlos López', 12]]

# Diccionario de (Marca, Modelo): precio
precios = {
  ("Toyota", "Corolla"): 10000,
  ("Honda", "Civic"): 5000,
  ("Ford", "Mustang"): 3000,
  ("Chevrolet", "Cruze"): 8000,
  ("Honda", "Golf"): 1000
}



def crearDiccionarioVentasTotales(ventas):
  '''
  Recibe una lista de ventas:
  [ marca, modelo, int(cantidad vendida), vendedor, int(mes) ]

  Devuelve un diccionario:
  { vendedor: int( total vendido )}
  '''

  """"""
  
  # Completar punto 1
  venta_ordenada=sorted(ventas,key=lambda item: item[3])
  venta_Total = {}
  datos = []
  for venta in venta_ordenada:
    datos.append([venta[3],venta[2]])
    
  datos_ventas=dict(datos)
  
       


  
  return print("Ventas por vendedor", datos_ventas)


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

  return {
    "Marcos": 1000,
    "Juan": 880
  }