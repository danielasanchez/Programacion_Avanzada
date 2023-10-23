# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

def obtener():
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
    
    

def update():
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
    
    
principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x450+400+200")
principal.config(bg="gray")

#variable de control String, Int, Double, Boolean
opcion=IntVar() 
#se le establece una opcion por default
# opcion.set(0)
etiqueta1 = StringVar()
etiqueta1.set("Nombre")
etiqueta2 = StringVar()
etiqueta2.set("atributo hijo")

inputPadre = StringVar()
inputHijo = StringVar()

label1 = Label(principal,  font=("Arial",16,"bold"),text="Elegir")
label1.pack()
label1.config(width=10,bg="gray",pady=20)

opcion1 = Radiobutton(principal,text="Persona",
                      font=("Arial",14,"bold"),
                      bg="gray",variable=opcion,value=1,
                      command=update).pack()
opcion2 = Radiobutton(principal,text="Medico",
                      font=("Arial",14,"bold"),
                      bg="gray",variable=opcion,value=2,
                      command=update).pack()
opcion2 = Radiobutton(principal,text="Paciente",
                      font=("Arial",14,"bold"),
                      bg="gray",variable=opcion,value=3,
                      command=update).pack()


label2 = Label(principal, textvariable=etiqueta1)
label2.pack()
label2.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))

input1 = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               textvariable=inputPadre)
input1.pack()


label3 = Label(principal, textvariable=etiqueta2)
label3.pack()
label3.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))

input2 = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               textvariable=inputHijo)
input2.pack()



boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                font=("Arial",16,"bold"),
                #state=DISABLED
                )

boton1.place(x=120,y=350)
boton1.config(pady=5,width=10)




principal.mainloop()

