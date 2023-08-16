def factorial (numero):
    if numero<0:
        fact=0
    else:
        fact=1
        for elemento in range(1,numero+1,1):
            fact=fact*elemento
    return fact
print(factorial(3))
print(factorial(10))    
print(factorial(0))
print(factorial(4))
