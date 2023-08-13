import random

def generar(a,b):
    '''
    generar aleatorio
    
    '''
    return random.randint(a,b)

num_gen=(generar(1,100))
print(num_gen)



num_adiv=int(input("adivina el numero:"))

while num_adiv!=num_gen:
    if num_adiv<num_gen:
        print("EL NUMERO ES MAYOR")
    elif num_adiv>num_gen:
        print("EL NUMERO ES MENOR")
    num_adiv=int(input("adivina el numero:"))

print("adivinaste el numero :)")
