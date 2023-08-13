def numMes (numero):
    mes="numero invalido"
    if numero==1:
        mes="enero"
    if numero==2:
        mes="febrero"
    if numero==3:
        mes="marzo"
    if numero==4:
        mes="abril"
    if numero==5:
        mes="mayo"
    if numero==6:
        mes="junio"
    if numero==7:
        mes="julio"
    if numero==8:
        mes="agosto"
    if numero==9:
        mes="septiembre"
    if numero==10:
        mes="octubre"
    if numero==11:
        mes="noviembre"
    if numero==12:
        mes="diciembre"
    return mes
print(numMes(1))
print(numMes(5))
print(numMes(10))
print(numMes(20))
