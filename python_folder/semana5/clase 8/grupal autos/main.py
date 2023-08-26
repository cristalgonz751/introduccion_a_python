from imprimir import imprimirTotal, imprimirVentas
from calcular import crearDiccionarioVentasTotales, crearDiccionarioGananciasTotales

# Lista con marca, modelo, cantidad vendida, vendedor, mes
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

print("Ventas")
imprimirVentas(ventas)


print("\nCantidad total de autos vendidos por cada vendedor")
ventasPorVendedor = crearDiccionarioVentasTotales(ventas)
imprimirTotal(ventasPorVendedor)


print("\nGanancia total de autos vendidos por cada vendedor")
gananciasPorVendedor = crearDiccionarioGananciasTotales(ventas, precios)
imprimirTotal(gananciasPorVendedor)
