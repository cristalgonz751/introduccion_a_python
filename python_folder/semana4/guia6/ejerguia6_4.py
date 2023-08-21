'''
1. Utilizar una función lambda para realizar el ordenamiento de forma ascendente.
2. Realizar el mismo ordenamiento pero en forma descendente.

'''

personas = [
("Ana", 28),
("Carlos", 23),
("María", 35),
("Luis", 19),
("Laura", 42)
]

def	orden(tabla,updown):
    orden=tabla.sort(reverse=updown ,key=lambda item: item[1])
    return tabla
updown=True
ordenup=orden(personas,updown)
print(ordenup)
updown=False
ordendown=orden(personas,updown)
print(ordendown)