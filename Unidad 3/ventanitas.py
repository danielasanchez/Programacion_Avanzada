# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:11:13 2023

@author: AlumnoFCA
"""

from tkinter import *


def obtener(*args):
    opcion=args[0]
    etiqueta2=args[1]
    inputPadre=args[2]
    inputHijo=args[3]
    
    print(opcion.get())
    opcion.set(0)
    etiqueta2.set("atributo hijo")
    print("El nombre es",inputPadre.get())
    print("El atributo hijo es",inputHijo.get())
    # aqui ya empiezan a crear las instancias
    # nombre = inputPadre.get()
    # padecimientos = inputHijo.get()
    # persona = Persona(nombre)
    # paciente = Paciente(nombre,padecimientos)
    
    

def update(opcion,etiqueta2,input1,input2,inputHijo):
    clase = opcion.get()
    if clase==1:
        etiqueta2.set("No aplica")
        input2.config(state= "disabled")#readonly
        inputHijo.set("No aplica")
        input1.focus_set()
        
    elif clase==2:
        etiqueta2.set("Especialidad")
        input2.config(state= "normal")
        inputHijo.set("")
    elif clase == 3:
        etiqueta2.set("Padecimientos")
        input2.config(state= "normal")
        inputHijo.set("")
    
    

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
    

def ventanita3(principal):
    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(principal)
    ventana.title("Mi ventanita 3")
    ventana.geometry("380x450+400+200")
    ventana.config(bg="gray")
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    #variable de control String, Int, Double, Boolean
    opcion=IntVar() 
    #se le establece una opcion por default
    opcion.set(0)
    etiqueta1 = StringVar()
    etiqueta1.set("Nombre")
    etiqueta2 = StringVar()
    etiqueta2.set("atributo hijo")
    
    inputPadre = StringVar()
    inputHijo = StringVar()
    
    label1 = Label(ventana,  font=("Arial",16,"bold"),text="Elegir")
    label1.pack()
    label1.config(width=10,bg="gray",pady=20)
    
    param = [opcion,etiqueta2]
    opcion1 = Radiobutton(ventana,text="Persona",
                          font=("Arial",14,"bold"),
                          bg="gray",variable=opcion,value=1,
                          command = lambda : update(opcion,etiqueta2,input1,input2,inputHijo)).pack()
                  
    opcion2 = Radiobutton(ventana,text="Medico",
                          font=("Arial",14,"bold"),
                          bg="gray",variable=opcion,value=2,
                          command = lambda : update(opcion,etiqueta2,input1,input2,inputHijo)).pack()
    opcion2 = Radiobutton(ventana,text="Paciente",
                          font=("Arial",14,"bold"),
                          bg="gray",variable=opcion,value=3,
                          command = lambda : update(opcion,etiqueta2,input1,input2,inputHijo)).pack()
    
    
    label2 = Label(ventana, textvariable=etiqueta1)
    label2.pack()
    label2.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))
    
    input1 = Entry(ventana, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green",
                   textvariable=inputPadre)
    input1.pack()
    
    
    label3 = Label(ventana, textvariable=etiqueta2)
    label3.pack()
    label3.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))
    
    input2 = Entry(ventana, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green",
                   textvariable=inputHijo)
    input2.pack()
    
    
    
    boton1 = Button(ventana, text="Obtener", bg="gray",
                    command= lambda : obtener(opcion,etiqueta2,inputPadre,inputHijo),
                    activebackground="yellow",
                    activeforeground="red",
                    font=("Arial",16,"bold"),
                    #state=DISABLED
                    )
    
    boton1.place(x=120,y=350)
    boton1.config(pady=5,width=10)