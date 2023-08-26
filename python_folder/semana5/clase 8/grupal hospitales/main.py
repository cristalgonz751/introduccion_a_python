from imprimir import  imprimirPlanillas,imprimirTotal,imprimirIndice
from calcular import crearDiccionarioHyHxLocalidad, crearDiccionarioIndice

# Lista con localidad, centros dervicios salud, cantidad habitantes, mes
planilla1 = [['Oberá', 63310, 1],
            ['Candelaria', 13777, 1],
            ['Apóstoles', 26710, 1],
            ['Posadas', 275028, 1],
            ['Jardín América', 22762,1],
            ['Montecarlo', 18827, 1],
            ['Puerto Esperanza', 15204, 1],
            ['Puerto Rico', 15995 , 1],
            ['Aristóbulo del Valle', 15918, 1]]

planilla2 = [['Wanda', 13901, 1],
            ['Posadas', 275028, 1],
            ['Posadas', 275028 , 1],
            ['Montecarlo', 18827, 1],
            ['Puerto Rico', 15995 , 1],
            ['San Vicente', 21068, 1],
            ['Oberá', 63310, 1],
            ['Apóstoles', 26710, 1],
            ['Eldorado', 60521, 2],
            ['Puerto Iguazú', 41062, 1],
            ['San Vicente', 21068, 1],
            ['Oberá', 63310, 1],
            ['Jardín América', 22762,1]]

planilla3 = [['Apóstoles', 26710, 1],
            ['Puerto Esperanza', 15204, 1],
            ['Aristóbulo del Valle', 15918, 1],
            ['Posadas', 275028, 1],
            ['Montecarlo', 18827, 1],
            ['Leandro N. Alem', 23339, 1]]

planillas=[planilla1,planilla2,planilla3]
print("planillas")
imprimirPlanillas(planillas)


print("\nCantidad total de habitantes y hospitales por localidad")
datosPorLocalidad = crearDiccionarioHyHxLocalidad(planillas)
imprimirTotal(datosPorLocalidad)


print("\nListado de mayor a menos de las 5 localidades de mayor indice habitantes/hospitales")
ListadoOrdenadoIndiceHabHos = crearDiccionarioIndice(datosPorLocalidad)
imprimirIndice(ListadoOrdenadoIndiceHabHos)
