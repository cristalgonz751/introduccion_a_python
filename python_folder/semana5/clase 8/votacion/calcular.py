def crearDiccionarioNacional():
    votacion_nacional={}
    seguir=True
    while    seguir:
        provincia=''
        votosPartido={}
        provincia=(input('Ingrese nombre de la Provincia:')).upper()
       
        if provincia!='FIN':
            partido=(input('Ingrese nombre de la Partido Político:')).upper()
            votos=int(input('Ingrese nombre de la Cantidad de Votos:'))
            if provincia not in votacion_nacional:   
                    votosPartido[partido]=votos
                    votacion_nacional[provincia]=votosPartido
            else:
                votosPartido=votacion_nacional[provincia]
                if partido not in votosPartido:    
                    votosPartido[partido]=votos
                    votacion_nacional[provincia]=votosPartido
                else:
                    votosPartido[partido]+=votos
                    votacion_nacional[provincia]=votosPartido
        else:
            seguir=False 

    return votacion_nacional

def crearPartidoProvincia(votacion_nacional):
    votosPartidoProvincia=[]
    for provincia in votacion_nacional:
        
        votacionPartidos=votacion_nacional[provincia].items()
        votacionPartidos=sorted(votacionPartidos,key=lambda item: item[1],reverse=True)
        partidoGanador=votacionPartidos[0]
        totalProvincia=0
        for partido in votacionPartidos:
            totalProvincia+=partido[1]
        porcentaje=partidoGanador[1]*100/totalProvincia
        votosPartidoProvincia.append([provincia,partidoGanador,porcentaje])
    votosPartidoProvincia.sort(key=lambda item: item[0],reverse=True)
    return votosPartidoProvincia

def crearPartidoNacional(votacion_nacional):
    votosPartidoNacional={}
    totalvotos=0
    for provincia in votacion_nacional:
        for partido in votacion_nacional[provincia]:
            totalvotos+= votacion_nacional[provincia][partido] 
            if partido not in votosPartidoNacional:
                votosPartidoNacional[partido]= votacion_nacional[provincia][partido] 
                
            else:
                votosPartidoNacional[partido]+= votacion_nacional[provincia][partido]
            
    for partido in votosPartidoNacional:
        votosPartidoNacional[partido]=(votosPartidoNacional[partido],votosPartidoNacional[partido]*100/totalvotos)
    
    votosPartidoNacional=votosPartidoNacional.items()
    votosPartidoNacional=sorted(votosPartidoNacional,key=lambda item: item[1][0],reverse=True)
    

    return votosPartidoNacional