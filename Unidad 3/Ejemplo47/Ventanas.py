# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:38:53 2023

@author: Daniela
"""

from tkinter import *

def cerrarSesion(ventana):
     ventana.destroy()
     #regresamos a la funcion inicial
     #no puedo llamar directo a ventanaLogin
     #ya que esa ventana necesita los usuarios
     #y necesitamos main para tener esa informacion
     import Ejemplo47
     Ejemplo47.main()
     # VentanaLogin()
     
def regresar(ventana,u):
     ventana.destroy()
     #invoco nuevamente la ventana inicial enviandole
     #el usuario (u) logueado
     import VentanaPrincipal
     VentanaPrincipal.VentanaPrincipal(u)
     # VentanaLogin()
     

     
     
def VentanaAzul(u):

         
    Azul = Tk()
    Azul.title("Ventana azul")
    Azul.geometry("380x280+400+200")
    Azul.config(bg="blue")
    Azul.resizable(0,0)  
    label1 = Label(Azul, text="Hola "+u.name,bg='blue')
    label1.pack()
    
    boton1 = Button(Azul, text="Anterior", bg="gray",
                command=lambda:regresar(Azul,u),
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )
    boton1.place(x=150,y=130)
    boton1.config(pady=10,width=10)
    
    boton2 = Button(Azul, text="Cerrar Sesion", bg="gray",
                command=lambda:cerrarSesion(Azul),
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

    boton2.place(x=150,y=190)
    boton2.config(pady=10,width=10)
    
    
    Azul.mainloop()
    
def VentanaVerde(u):
    Verde = Tk()
    Verde.title("Ventana azul")
    Verde.geometry("380x280+400+200")
    Verde.config(bg="green")
    Verde.resizable(0,0)

    label1 = Label(Verde, text="Hola "+u.name,bg='green')
    label1.pack()
    
    boton1 = Button(Verde, text="Anterior", bg="gray",
                command=lambda:regresar(Verde,u),
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )
    
    boton1.place(x=150,y=130)
    boton1.config(pady=10,width=10)
    
    boton2 = Button(Verde, text="Cerrar Sesion", bg="gray",
                command=lambda:cerrarSesion(Verde),
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

    boton2.place(x=150,y=190)
    boton2.config(pady=10,width=10)
    

    Verde.mainloop()