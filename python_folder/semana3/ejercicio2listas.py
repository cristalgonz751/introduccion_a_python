def ingreso(lista):
    valor='1'
    while valor!='0':
        valor=(input('Ingrese un valor: '))
        if validar(valor)==True:
            lista+=[int(valor)]
    return lista

def validar(valor):
    if valor.isnumeric(): 
        return True
    else:
        print('Ingreso invalido')
        return False

lista=[]
lista=ingreso(lista)
lista.pop(-1)
print(lista)
