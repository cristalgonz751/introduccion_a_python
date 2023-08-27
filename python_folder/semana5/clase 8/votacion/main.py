
'''
Guía de ejercicios del material de la cátedra:

7. Escribir un programa que permita administrar los datos de una votación electoral. 
Para ello, será necesario que nuestro programa cumpla los siguiente requerimientos: 

a) Gestionar la carga de datos de la votación, almacenando los datos en un diccionario 
de diccionarios,
 que tendrá el siguiente formato:
{ provincia: { partido_politico: votos_obtenidos ,,,,,} ,,,,}
- Por cada una de las provincias, tendremos la cantidad de votos obtenidos para cada uno
 de los partidos políticos.
- La carga de datos debe solicitar, la Provincia, el Partido Político, y la cantidad 
de votos.
- Puede haber más de un ingreso de cantidad de votos, para una misma Provincia y 
Partido Político, en ese caso se deben acumular a los ya existentes.
- La carga finaliza cuando se ingrese como nombre de Provincia, la palabra FIN. 

b) Informar para cada Provincia que Partido obtuvo más votos, indicando la cantidad de 
votos y el porcentaje que representan sobre el total de las votaciones de la provincia.
 El listado debe estar ordenado por el nombre de la Provincia. 

c) Informar el ranking de votos a nivel Nacional por Partido Político. El listado debe
 estar ordenado de mayor a menor por la cantidad de votos obtenidos, y debe figurar el
  Partido Político, la cantidad de votos obtenidos, y el porcentaje respecto del total
   de votos.

'''
from imprimir import imprimirPartidoProvicia,imprimirPartidoNacional 
from calcular import crearDiccionarioNacional,crearPartidoProvincia,crearPartidoNacional


print('Se le solicitará el ingreso de datos\n para Finalizar escriba FIN como nombre de Provincia')
votacionNacional=crearDiccionarioNacional()

print('Informe de Partido mas votado y su % por Provincia ')
votosPartidoProvinciaPorcentaje=crearPartidoProvincia(votacionNacional)
imprimirPartidoProvicia(votosPartidoProvinciaPorcentaje)

print('Ranking de votos x Partido a Nivel Nacional y sus %  ')
votosPartidoNacionalPorcentaje=crearPartidoNacional(votacionNacional)
imprimirPartidoNacional(votosPartidoNacionalPorcentaje)
print(votosPartidoNacionalPorcentaje)
