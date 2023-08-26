def imprimirVentas(ventas):
  # Impresion en forma de tabla
  for venta in ventas:
    print(
      str(venta[2]).center(5), '|', venta[0].ljust(10), '|',
      venta[1].ljust(10), '|', venta[3].ljust(20), '|', venta[4])


def imprimirTotal(ventasPorVendedor):
  '''
    Recibe un diccionario y lo imprime con la siguiente estructura:
    ventasPorVendedor = {
        vendedor1 : cantidad1,
        vendedor2 : cantidad2,
        ...
    }
    '''
  for vendedor, cantidad in ventasPorVendedor.items():
    print(vendedor.ljust(20), '|', str(cantidad).ljust(10))
