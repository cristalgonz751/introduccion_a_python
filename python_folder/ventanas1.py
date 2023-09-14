from tkinter import *
raiz=Tk()
raiz.title('ventana cris')
raiz.iconbitmap('python_folder\semana6\gui\communication_network_wifi_signal_router_icon_256499.ico')

#raiz.resizable(True,True)
#raiz.geometry('640x480')
raiz.config(bg='green')
miframe=Frame()

miframe.pack(fill='both',expand='True')
miframe.config(bg='blue')
miframe.config(width='640',height='480')
miframe.config(relief='groove')
miframe.config(bd=35)
nombreLabel=Label(miframe,text='Nombre:')
nombreLabel.grid(row=0,column=0,sticky='e',padx=10,pady=10)
entry_nombre=Entry(miframe)
entry_nombre.grid(row=0,column=1,sticky='e',padx=10,pady=10)

raiz.mainloop()
