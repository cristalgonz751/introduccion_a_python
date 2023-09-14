def es_primo(numero):
    if(numero==1 or numero%2==0 or numero%3==0 or numero%5==0 or numero%7==0):
        if (numero==1 or numero==2 or numero==3 or numero==5 or numero==7):
            print('el numero %s es primo'%numero)
        else :
            print('el numero %s no es primo'%numero)
    else:
        print('el numero %s es primo'%numero)
    return

es_primo(int(input('ingrese numero:')))