def imprimirPlanillas(planillas):
  # Impresion en forma de tabla
  for planilla in planillas:
    print('\n')
    for registro in planilla:
      print(
        registro[0].ljust(20), '|', str(registro[1]).center(10), '|',
        registro[2] )


def imprimirTotal(datosPorLocalidad):
  '''
    Recibe un diccionario y lo imprime con la siguiente estructura:
    ventasPorVendedor = {
        Localidad1 : habitantes1,hospitales1
        Localidad1 : habitantes1,hospitales1
        ...
    }
    '''
  for localidad in datosPorLocalidad.items():
    print(localidad[0].ljust(20), '|', str(localidad[1][0]).ljust(10), '|', str(localidad[1][1]).ljust(10))

def imprimirIndice(datosPorLocalidadIndices):
  for localidad,indice in datosPorLocalidadIndices.items():
    print(localidad.ljust(20), '|', str(indice).ljust(10))

