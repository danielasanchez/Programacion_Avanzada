# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:11:13 2023

@author: AlumnoFCA
"""

from tkinter import *


label={}
button={}
names=[]
frameRegistros={}



class Perro():# nombre="Whisky"# raza = "Chihuahua"# edad = 11
    def __init__(self,id,nombre,raza,edad,idpropietario=""):
        self.id=id
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        print("Objeto Creado")
        
             
perrito1=Perro(1,"Whisky","Chihuahua",11)
perrito2=Perro(2,"Tequila","Chihuahua",10)
perrito3=Perro(3,"Akira","Mestizo",11)
perrito4=Perro(4,"Princesa","Labrador",10)
perrito5=Perro(5,"Sakura","Mestizo",11)
perrito6=Perro(6,"Pulga","Labrador",10)

perritos=[perrito1,perrito2,perrito3,perrito4,perrito5,perrito6]


def registro(idx_and_item,frame,ventana):
    index, item = idx_and_item
    lb1 = Label(frame, text="id: "+str(item.id))
    lb1.grid(row=index, column=1)
    lb1 = Label(frame, text="Nombre: "+item.nombre)
    lb1.grid(row=index, column=2)
    lb2 = Label(frame, text="Edad: "+str(item.edad))
    lb2.grid(row=index, column=3)
    bt1 = Button(frame, text="Registrar", command= lambda : ventanitaRegistro (ventana,item))
    bt1.grid(row=index, column=4)

#es funcion usara un map para ir mostrando cada uno de los registros    
def filtrados(arreglo,frame,ventana):
    if len(arreglo)>0:
        result = list(map(lambda e: registro(e,frame,ventana), enumerate(arreglo)))

    
def update(opcion,perros,ventana,frame):
    # limpiamos cualquier widget que este en el frame
    for widgets in frame.winfo_children():
        widgets.destroy()

    clase = opcion.get()
    if clase==1:
        #filtramos aquellos objetos que cumplan con la condicion
        arreglo = list(filter(lambda e: e.raza=="Chihuahua",perros))
        #mandamos llamar la funcion 
        filtrados(arreglo,frame,ventana)
    elif clase==2:
        arreglo = list(filter(lambda e: e.raza=="Labrador",perros))
        filtrados(arreglo,frame,ventana)
    elif clase==3:
        arreglo = list(filter(lambda e: e.raza=="Mestizo",perros))
        filtrados(arreglo,frame,ventana)         


def ventanita1(principal):
    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(principal)
    ventana.title("Mi ventanita 1")
    ventana.geometry("180x80+500+300")
    # minsize(x,y)
    # maxsize(x,y)
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    # podemos agregar widgets
    label1 = Label(ventana, text="Soy una etiqueta")
    label1.pack()
    input1 = Entry(ventana, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green")
    input1.pack()    
    
def ventanita2(principal):
    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(principal)
    ventana.title("Mi ventanita 2")
    ventana.geometry("280x180+450+250")
    # minsize(x,y)
    # maxsize(x,y)
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    # podemos agregar widgets
    label1 = Label(ventana, text="Soy una etiqueta")
    label1.pack()
    input1 = Entry(ventana, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green")
    input1.pack()    
    

def ventanitaFiltro(principal):
    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(principal)
    ventana.title("Mi ventanita 3")
    ventana.geometry("380x450+400+200")
    # ventana.config(bg="gray")
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    #variable de control String, Int, Double, Boolean
    opcion=IntVar() 
    #se le establece una opcion por default
    opcion.set(0)
    
    label1 = Label(ventana,  font=("Arial",16,"bold"),text="Elegir")
    label1.pack()
    label1.config(width=10,pady=20)
    

    opcion1 = Radiobutton(ventana,text="Chihuahua",
                          font=("Arial",14,"bold"),
                          variable=opcion,value=1,
                          command = lambda : update(opcion,perritos,ventana,frame)).pack()
                  
    opcion2 = Radiobutton(ventana,text="Labrador",
                          font=("Arial",14,"bold"),
                          variable=opcion,value=2,
                          command = lambda : update(opcion,perritos,ventana,frame)).pack()
    opcion2 = Radiobutton(ventana,text="Mestizo",
                          font=("Arial",14,"bold"),
                          variable=opcion,value=3,
                          command = lambda : update(opcion,perritos,ventana,frame)).pack()
    #se crea este frame donde se pondran los widgets
    #para cada registro, con la finalidad de poder borrarlos
    #mas facilmente cuando se actualice la seleccion, 
    #mandandolo por parametro en los radiobuttons
    frame = Frame(ventana)
    frame.pack()
    

    
#se le asigna None por default para poder utilizar la misma ventada
#donde posiblemente no se tenga ese dato.
def ventanitaRegistro(ventanaAnterior,objeto=None):
    
    if objeto == None:
        estado = NORMAL
    else:
        estado = DISABLED
        
    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(ventanaAnterior)
    ventana.title("Registro")
    ventana.geometry("380x450+400+200")
    # ventana.config(bg="gray")
    # minsize(x,y)
    # maxsize(x,y)
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=ventanaAnterior)
    
    idmascota=IntVar()
    nombre = StringVar()
    raza = StringVar()
    edad = IntVar()

    # sacamos la informacion del objeto
    if objeto:
        idmascota.set(objeto.id)
        nombre.set(objeto.nombre)
        raza.set(objeto.raza)
        edad.set(objeto.edad)

    else:
        idmascota.set("")
        nombre.set("")
        raza.set("")
        edad.set("")

        
    label1 = Label(ventana,  font=("Arial",16,"bold"),text="Registro")
    label1.pack()
    label1.config(width=10,pady=20)
    
    
    # podemos agregar widgets
    frame1 = Frame(ventana)
    frame1.pack()
    
    label2 = Label(frame1, text="Id Mascota")
    label2.grid(row=1, column=1)
    label2.config(font=("Arial",16,"bold"))
    
    input1 = Entry(frame1, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               textvariable=idmascota, state=estado)
    input1.grid(row=1, column=2)
    
    
    label2 = Label(frame1, text="Nombre Mascota")
    label2.grid(row=2, column=1)
    label2.config(font=("Arial",16,"bold"))
    
    input1 = Entry(frame1, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               textvariable=nombre)
    input1.grid(row=2, column=2)
    
    
    label3 = Label(frame1, text="Raza")
    label3.grid(row=3, column=1)
    label3.config(font=("Arial",16,"bold"))
    
    input1 = Entry(frame1, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               textvariable=raza)
    input1.grid(row=3, column=2)
    
    
    label4 = Label(frame1, text="Edad")
    label4.grid(row=4, column=1)
    label4.config(font=("Arial",16,"bold"))
    
    input1 = Entry(frame1, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               textvariable=edad)
    input1.grid(row=4, column=2)
    
    
    boton1 = Button(ventana, text="Hola", bg="gray",
                    # command= lambda objeto: objeto.idpropietario = idpropietario,
                    activebackground="yellow",
                    activeforeground="red",
                    font=("Arial",16,"bold"),
                    #state=DISABLED
                    )
    
    boton1.place(x=120,y=350)
    boton1.config(pady=5,width=10)
    
    
    
    
    
    
