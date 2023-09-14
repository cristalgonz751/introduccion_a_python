#Grupo 1 parte 2
# https://replit.com/@FrancoGarcia12/Grupo1-Parte-2-Ejercicio?from=notifications#main.py
import csv


def cifrar_mensaje(mensaje, tipo, clave=None):
  mensaje_cifrado = ""
  if tipo == "1":
    mensaje_cifrado = cifrar_atbash(mensaje)
  elif tipo == "2":
    mensaje_cifrado = cifrar_cesar(mensaje, clave)
  return mensaje_cifrado


def descifrar_mensaje(mensaje, tipo, clave=None):
  mensaje_descifrado = ""
  if tipo == "1":
    mensaje_descifrado = descifrar_atbash(mensaje)
  elif tipo == "2":
    mensaje_descifrado = descifrar_cesar(mensaje, clave)
  return mensaje_descifrado


def cifrar_atbash(mensaje):
  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  mensaje_cifrado = ""
  for letra in mensaje:
    if letra.isalpha():
      if letra.isupper():
        mensaje_cifrado += alfabeto[25 - alfabeto.index(letra)]
      else:
        mensaje_cifrado += alfabeto[25 - alfabeto.index(letra.upper())].lower()
    else:
      mensaje_cifrado += letra
  return mensaje_cifrado


def descifrar_atbash(mensaje):
  return cifrar_atbash(mensaje)


def cifrar_cesar(mensaje, clave):
  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  mensaje_cifrado = ""
  for letra in mensaje:
    if letra.isalpha():
      if letra.isupper():
        mensaje_cifrado += alfabeto[(alfabeto.index(letra) + clave) % 26]
      else:
        mensaje_cifrado += alfabeto[(alfabeto.index(letra.upper()) + clave) %
                                    26].lower()
    else:
      mensaje_cifrado += letra
  return mensaje_cifrado


def descifrar_cesar(mensaje, clave):
  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  mensaje_descifrado = ""
  for letra in mensaje:
    if letra.isalpha():
      if letra.isupper():
        mensaje_descifrado += alfabeto[(alfabeto.index(letra) - clave) % 26]
      else:
        mensaje_descifrado += alfabeto[(alfabeto.index(letra.upper()) - clave)
                                       % 26].lower()
    else:
      mensaje_descifrado += letra
  return mensaje_descifrado


def cifrar_en_consola():
  tipo = input(
      "Seleccione el tipo de cifrado\n1)Atbash\n2)César\n").capitalize()
  mensaje = input("Introduce el mensaje a cifrar: ")

  if tipo == "2":
    clave = int(input("Introduce la clave para César: "))
  else:
    clave = None

  mensaje_cifrado = cifrar_mensaje(mensaje, tipo, clave)
  print("Mensaje cifrado:", mensaje_cifrado)
  if tipo =='2':
    tipo='C'
  else: tipo="A"
  #clave=str(clave)
  return mensaje_cifrado, tipo ,clave ### el print no va a molestar en este caso?


def descifrar_en_consola():
  tipo = input(
      "Seleccione el tipo de descifrado\n1)Atbash\n2)César\n").capitalize()
  mensaje = input("Introduce el mensaje a descifrar: ")

  if tipo == "2":
    clave = int(input("Introduce la clave para César: "))
  else:
    clave = None

  mensaje_descifrado = descifrar_mensaje(mensaje, tipo, clave)
  print("Mensaje descifrado:", mensaje_descifrado)


#------------------------------------- aqui pondremos el metodo para verificar al espia
def verificar_destinatario(destinatario):
  #aqui tenemos que verificar si el espia existe
  if destinatario == '*':
    return True
  if len(destinatario) >= 5 and len(destinatario) <= 15:
    for caracter in destinatario:
      if not (caracter.isalnum() or caracter in "_-."):
        #print(caracter)
        return False
    return True
  return False


def guardar_mensaje(destinatario, cifrado,clave, mensaje_cifrado):
  with open('./semana7/mensaje_seceto_grupo1/mensajes.csv', mode='a', newline='') as archivo:
    wr = csv.writer(archivo)
    if clave==None:
      wr.writerow([destinatario, cifrado, mensaje_cifrado])
    else:
      wr.writerow([destinatario, cifrado,clave, mensaje_cifrado])

def enviar_mensajes():
  destinatario = input("Ingrese al espia que desea enviar el mensaje: ")
  if verificar_destinatario(destinatario):
    print("Destinatario Valido.")
    mensaje_cifrado, tipo,clave = cifrar_en_consola()
    guardar_mensaje(destinatario, tipo,clave, mensaje_cifrado)
    print("Mensaje guardado")
  else:
      print("Destinatario invalido o inexistente")
#---------------------------------------------------------------


def main():
  while True:
    opcion = input(
        "Seleccione una opción\n1)Cifrar\n2)Descifrar\n3)Enviar mensaje cifrado\n4)Salir\n"
    ).capitalize()

    if opcion == "4":
      break
    elif opcion == "1":
      cifrar_en_consola()
    elif opcion == "2":
      descifrar_en_consola()
    elif opcion == "3":
      enviar_mensajes()
 
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
  main()
