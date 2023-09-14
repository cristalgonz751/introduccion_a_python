y=4
x=y//2
print(type(x))


def factorial(numero):
    resultado=0
    if numero>=0:
        resultado=1
        for valor in range(2,numero+1):
            resultado*=valor
        return resultado

print(factorial(0))