# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

def obtener():
    print(nombre.get())
    print(carrera.get())
    nombre.set("")
    carrera.set(None)


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x380+400+200")
principal.config(bg="gray")

#StringVar, IntVat DoubleVar, BooleanVar
nombre = StringVar()
carrera = StringVar() 
carrera.set("LA")

label1 = Label(principal, text="Alumno:")
label1.pack()
label1.config(width=50,bg="gray",pady=20)

nombre.set("Daniela")
input1 = Entry(principal,textvariable=nombre,width=35).pack()

label2 = Label(principal, text="Carrera:")
label2.pack()
label2.config(width=10,bg="gray",pady=20)


opcion1 = Radiobutton(principal,text="Lic. Inteligencia de Negocios",
                      bg="gray",variable=carrera,value="LIN",
                      activebackground="pink",activeforeground="blue",
                      selectcolor="yellow").pack()
opcion2 = Radiobutton(principal,text="Lic. Contaduria",
                      bg="gray",variable=carrera,value="LC",
                      activebackground="pink",activeforeground="blue",
                      selectcolor="yellow").pack()
opcion3 = Radiobutton(principal,text="Lic. Administracion",
                      bg="gray",variable=carrera,value="LA",
                      activebackground="pink",activeforeground="blue",
                      selectcolor="yellow").pack()
opcion4 = Radiobutton(principal,text="Lic. Negocios Internacionales",
                      bg="gray",variable=carrera,value="LNI",
                      activebackground="pink",activeforeground="blue",
                      selectcolor="yellow").pack()



boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=150,y=280)
boton1.config(pady=10,width=10)


principal.mainloop()

