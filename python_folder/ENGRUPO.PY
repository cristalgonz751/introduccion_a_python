#SALA DE TRABAJO 5
import csv
from tkinter import *
from tkinter import messagebox


def obtener_usuarios_claves():
   # ruta_archivo = 'usuarios.csv'
    integrantes={}
    #integrantes={"Nicolas": "12345", "Cristian": "Gonzalez", "Juan": "6789"}
    with open('usuarios.csv',mode='r') as archivo:
        reader=csv.reader(archivo) 

        encabezado=next(reader) 
        for usuario,password in reader:
            integrantes[usuario]=password  


    return integrantes


        
def registrarUsuarios(usuario, clave):  
    with open('usuarios.csv',mode='a',newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([usuario,clave])
    

def validarUsuario(usuario, clave):
    usuariosClave=obtener_usuarios_claves()
    
    if usuario in usuariosClave and usuariosClave[usuario] == clave:
        
        messagebox.showinfo("Datos ingresados", "Usuario y clave correctos")
        

    
    else:
        messagebox.showerror("Error", "Alguno de los datos ingresado es incorrecto")
'''
También debemos controlar que el nombre de usuario ingresado no exista y que la clave esté compuesta al menos por 8 
caracteres entre los cuales al menos debe haber un número, un letra mayúscula y un letra minúscula. No es posible utilizar
 otro tipo de caracter, salvo los siguientes: "_" (guion bajo) "*" asterisco "guion medio".
Los datos deben ser guardados en el archivo csv donde se encuentran las claves y que utilizamos en la actividad 1.
'''    
    
def registrarUsuario(usuario, clave):
    usuariosClave=obtener_usuarios_claves()
    if usuario not in usuariosClave:
        if len(clave)>=8:    
            while                           #mayor a 8 caracteres
            if min(clave).isupper()==True:                #al menos una mayuscula
                if max(clave).islower()==True:            #al menos una minuscula
                    if clave.isalnum()==True              #alphanumerico


        
        registrarUsuarios(usuario, clave)
        messagebox.showinfo("Registro","Usuario y clave registrado")
    else:
        messagebox.showerror("Error", "usuario ya existe")
    return    

raiz = Tk()

raiz.title("Login Sala de Trabajo 5")
raiz.geometry("300x130")
raiz.resizable(False,False)
#raiz.iconbitmap('python_folder\semana6\gui\communication_network_wifi_signal_router_icon_256499.ico')
raiz.config(bg="green")

miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(bg='green')

cuadroUsuarioAlumno=Entry(miFrame)
cuadroUsuarioAlumno.grid(row=0, column=1, padx=8, pady=4)

cuadroClave=Entry(miFrame, show="*")
cuadroClave.grid(row=1, column=1, padx=8, pady=4)

usuarioAlumnoLabel=Label(miFrame, text="Usuario Alumno: ")
usuarioAlumnoLabel.grid(row=0, column=0, sticky="e", padx=8, pady=4)

claveLabel=Label(miFrame, text="Clave: ")
claveLabel.grid(row=1, column=0, sticky="e", padx=8, pady=4)
'''
Ahora que logramos nuestra ventana de Login, deberemos validar el ingreso del usuario y la clave.
Primero escribiremos la función obtener_usuarios_claves(), que genere y devuelva un diccionario del tipo
{clave: valor}, siendo la clave el “usuario alumno”, y el valor, la clave de ingreso correspondiente. Generar
un diccionario con cada uno de los integrantes del grupo. No debe solicitar que se ingresen los datos por
teclado, simplemente genérenlo dentro del código de la función.
A continuación debemos validar el ingreso que se haga contra el diccionario que devuelve la función, si el
usuario y la clave son correctos, mostrar el mensaje: “Usuario y Clave Correctos”, de lo contrario, mostrar el
mensaje “Algunos de los datos ingresados es Incorrecto”.

'''
    
botonEnvio=Button(miFrame, text="Enviar", command=lambda:validarUsuario(cuadroUsuarioAlumno.get(), cuadroClave.get()))
botonEnvio.grid(row=2, column=1, sticky="w")

botonRegistrar=Button(miFrame, text="Registrar", command=lambda:registrarUsuario(cuadroUsuarioAlumno.get(), cuadroClave.get()))
botonRegistrar.grid(row=3, column=1, sticky="w")


    

raiz.mainloop()

'''
#SALA DE TRABAJO 5

from tkinter import *
from tkinter import messagebox


def obtener_usuarios_claves():
    
    integrantes={"Nicolas": "12345", "Cristian": "Gonzalez", "Juan": "6789"}
    
    return integrantes
    

def validarUsuario(usuario, clave):
    usuariosClave=obtener_usuarios_claves()
    
    if usuario in usuariosClave and usuariosClave[usuario] == clave:
    
        messagebox.showinfo("Datos ingresados", "Usuario y clave correctos")
    
    else:
        messagebox.showerror("Error", "Alguno de los datos ingresado es incorrecto")


raiz = Tk()

raiz.title("Login Sala de Trabajo 5")
raiz.geometry("300x130")
raiz.resizable(False,False)
raiz.iconbitmap("planeta.ico")
raiz.config(bg="green")

miFrame = Frame(raiz)
miFrame.config(bg="green")
miFrame.pack()


cuadroUsuarioAlumno=Entry(miFrame)
cuadroUsuarioAlumno.grid(row=0, column=1, padx=8, pady=4)

cuadroClave=Entry(miFrame, show="*")
cuadroClave.grid(row=1, column=1, padx=8, pady=4)

usuarioAlumnoLabel=Label(miFrame, text="Usuario Alumno: ")
usuarioAlumnoLabel.grid(row=0, column=0, sticky="e", padx=8, pady=4)

claveLabel=Label(miFrame, text="Clave: ")
claveLabel.grid(row=1, column=0, sticky="e", padx=8, pady=4)
   
   
    
botonEnvio=Button(miFrame, text="Enviar", command=lambda:validarUsuario(cuadroUsuarioAlumno.get(), cuadroClave.get()))
botonEnvio.grid(row=2, column=1, sticky="w")
'''