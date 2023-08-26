"""
-----------------------------------------------------------------------------
Escribir una función que reciba una palabra, y devuelva True, si la palabra
tiene diptongo, y False, en caso contrario.
Asumir que la palabra recibida, solo esta formada por letras.
En español dos vocales en contacto se articulan como diptongo cuando:
 1) una es cerrada (i u) átona (no acentuada) y la otra es abierta (a e o)
 y viceversa.
 2) ambas son cerradas, excepto si son iguales (como en chiita), donde
 forman un hiato.
-----------------------------------------------------------------------------
"""
def hay_diptongo(palabra):
 """
 Funcion que recibe una palabra y retorna True si la misma
 tiene diptongo, o False, si no lo tiene.
 >>> hay_diptongo("ciudad")
 True
 >>> hay_diptongo("autódromo")
 True
 >>> hay_diptongo("ruido")
 True
 >>> hay_diptongo("audiovisual")
 True
 >>> hay_diptongo("cual")
 True
 >>> hay_diptongo("renuncia")
 True
 >>> hay_diptongo("renunciá")
 True
 >>> hay_diptongo("renuncié")
 True
 >>> hay_diptongo("renunció")
 True
 >>> hay_diptongo("manual")
 True
 >>> hay_diptongo("ruiseñor")
 True
 >>> hay_diptongo("ansioso")
 True
 >>> hay_diptongo("ansiedad")
 True
 >>> hay_diptongo("estación")
 True
 >>> hay_diptongo("silla")
 False
 >>> hay_diptongo("mesa")
 False
 >>> hay_diptongo("búho")
 False
 """
 # Armado de la lista de posibles diptongos segun definicion

 l_diptongo = []
 for letra_1 in ["u", "i"]:
    for letra_2 in ["a", "e", "o", "á", "é", "ó"]:
        l_diptongo.append( letra_1 + letra_2 )
        l_diptongo.append( letra_2 + letra_1)
        l_diptongo.extend(["ui", "iu"])
 # Control de si alguno de los diptongos forma parte de la palabra
        devolver = True
        posicion = 0
        while posicion < len(l_diptongo) and l_diptongo[posicion] not in palabra:
            posicion += 1
            if posicion == len(l_diptongo):
                devolver = False

 return devolver
#----------------------- Bloque Principal ---------------------------#
import doctest
print(doctest.testmod())