valores=[]
valor_ocurrencia=[]
valores_info=[]
contador=0


while contador!=10:                                 #ingreso 10 valores
    valor=input("ingrese valores entre 20 y 40:") 
    if valor.isnumeric()==True:                     #valida ingreso
        valor=int(valor)
        if valor >=20 and valor <=40:
            valores.append(valor)                   #genera lista de valores validos
            contador+= 1
        else:  
            print('VALOR NO VALIDO')      
    else:
        print('NO INGRESO UN NUMERO')    

for valor in valores:                               #genera lista de valores y cantidad de ocurrencias
    if valor not in valor_ocurrencia:
        valor_ocurrencia.append(valor)
        valores_info.append([valor,valores.count(valor)])

        

#print(valor_ocurrencia)
for valor in valores_info:
    print('el numero: %s fue ingresado %s veces' %(valor[0],valor[1]))
