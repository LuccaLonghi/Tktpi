import tkinter as tk
from tkinter import ttk
import tkinter

contactos = [] #Esto es una lista en la cual agregaremos los contactos que creemos

def AgregarContacto(): #Aqui creamos la funcion con la cual agregaremos los contactos
    ContactoNom = CuadritoNombre.get() #Aqui tomamos el nombre del contacto
    ContactoNum = CuadritoNumero.get() #Aqui tomamos el numero del contacto
    contacto = {"Nombre": ContactoNom, "Numero": ContactoNum} #Aqui creamos un diccionario donde guardamos los valores del contacto
    contactos.append(contacto) #En este agregamos el diccionario a la lista de contactos
    treeview.insert("", tkinter.END, text=ContactoNom, values=(ContactoNum)) #Aqui agregamos el contacto al treeview

def EliminarContacto(): #Creamos la funcion para borrar un contacto
    Seleccion = treeview.selection() #Creamos la variable que nos permitira seleccionar que contacto borrar
    for item in Seleccion: #Aqui creamos la variable item que sera el contacto eliminado
        treeview.delete(item) #Borramos el item(Contacto) seleccionado

Ventanal = tk.Tk() #Creamos una ventana
Ventanal.title("Gestor de Contactos") #Le damos un titulo a la ventana
treeview = ttk.Treeview(columns=("Number")) #Creamos una columna en la ventana con el numero del contacto como valor
treeview.heading("#0", text="Nombre") #A la columna inicial le damos el nombre de "Nombre"
treeview.heading("Number", text="Numero") #A la columna que creamos le damos el nombre de "Numero"
tk.Label(None,text="Nombre").grid() #Agregamos una etiqueta con el texto "Nombre"
CuadritoNombre = tk.Entry(Ventanal) #Agregamos un cuadro de texto en el que agregamos el dato de el nombre
CuadritoNombre.grid(column=0, row=1) #Agregamos el cuadro a la ventana
tk.Label(None,text="Numero").grid(column=0, row=2) #Agregamos una etiqueta con el texto "Numero"
CuadritoNumero = tk.Entry(Ventanal) #Agregamos un segundo cuadro de texto en el que agregamos el dato de el numero
CuadritoNumero.grid(column=0, row=3) #Agregamos el cuadro a la ventana
BotonAgregar = tk.Button(text="Agregar Contacto", bg="green", command=AgregarContacto) #Creamos un boton color verde con el texto agregar contacto con el comando de mismo nombre
BotonEliminar = tk.Button(text="Eliminar Contacto", bg="red", command=EliminarContacto) #Creamos un segundo boton color rojo con el texto eliminar contacto con el comando de mismo nombre
BotonAgregar.grid(column=0, row=4) #Agregamos el primer boton a la ventana
BotonEliminar.grid(column=0, row=5) #Agregamos el segundo boton a la ventana
treeview.grid() #Aqui agregamos la vista treeview a la ventana?
Ventanal.mainloop() #Creamos un bucle en la ventana para mantenerla abierta indefinidamente