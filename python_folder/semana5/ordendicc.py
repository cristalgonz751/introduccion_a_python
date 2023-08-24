def ordenar_diccionario(diccionario):
  '''
  Esta funcion recibe un diccionario cuyos valores son numeros enteros y lo devuelve ordenado segun estos valores de mayor a menor.
  '''

  # Completar esta funcion
  lista_elementos=diccionario.items()
  lista_ordenada=sorted(lista_elementos,reverse=True, key=lambda item : item[1])
  
  
  

  
  return dict(lista_ordenada)

print(ordenar_diccionario({'banana':100,'pera':200,'naranja':50}))