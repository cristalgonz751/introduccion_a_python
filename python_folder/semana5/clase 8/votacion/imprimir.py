def imprimirPartidoProvicia(votosPartidoProvincia):
    for provincia,partidoGanador,porcentaje in votosPartidoProvincia:
        print(provincia.ljust(20), '|', partidoGanador[0].ljust(20), '|', str(partidoGanador[1]).ljust(10), '|', (str(porcentaje)+'%').ljust(10))

def imprimirPartidoNacional(votosPartidoNacional):
    for partido,cantidad_porcentaje in votosPartidoNacional:
        print(partido.ljust(20), '|', str(cantidad_porcentaje[0]).ljust(10), '|', (str(cantidad_porcentaje[1])+'%').ljust(10))


