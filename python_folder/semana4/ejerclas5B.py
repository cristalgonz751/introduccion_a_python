valores=[]
valor_ocurrencia=[]
valores_info=[]
contador=0


while contador!=10:
    valor=input("ingrese valores entre 20 y 40:") 
    if valor.isnumeric()==True:
        valor=int(valor)
        if valor >=20 and valor <=40:
            valores.append(valor)
            contador+= 1
        else:  
            print('VALOR NO VALIDO')      # PUNTO 2
    else:
        print('NO INGRESO UN NUMERO')    # PUNTO 2

for valor in valores:
    if valor not in valor_ocurrencia:
        valor_ocurrencia.append(valor)
        valores_info.append([valor,valores.count(valor)])

        

print(valor_ocurrencia)
print(valores_info)
