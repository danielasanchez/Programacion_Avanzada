# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:38:53 2023

@author: Daniela
"""
from tkinter import *
from Ventanas import VentanaVerde, VentanaAzul
# from VentanaAzul import VentanaAzul
from tkinter import messagebox


def VentanaPrincipal(u):
    # u es el usuario logueado

    def cerrarSesion():
        principal.destroy()
        #regresamos a la funcion inicial
        #no puedo llamar directo a ventanaLogin
        #ya que esa ventana necesita los usuarios
        #y aqui no los tengo
        import Ejemplo45
        Ejemplo45.main()
        # VentanaLogin()
    
    def obtener():
        
        print(opcion.get())
        if opcion.get()==1:
            principal.destroy()
            VentanaAzul(u)
            
        elif opcion.get()==2:
            principal.destroy()
            VentanaVerde(u)
            
        else:
            messagebox.showinfo("Error","Selecciona una opcion")
        
    
    principal = Tk()
    principal.title("Principal")
    principal.geometry("380x280+400+200")
    principal.config(bg="gray")
    principal.resizable(0,0)
    opcion=IntVar() 
    
    opcion.set(0)
    
    
    label1 = Label(principal, text="Elige una respuesta "+u.name)
    label1.pack()
    label1.config(bg="gray")
    
    
    opcion1 = Radiobutton(principal,text="Ventana Azul",
                          bg="gray",variable=opcion,value=1).pack()
    opcion2 = Radiobutton(principal,text="Ventana Verde",
                          bg="gray",variable=opcion,value=2).pack()
    
    boton1 = Button(principal, text="Siguiente", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

    boton1.place(x=150,y=130)
    boton1.config(pady=10,width=10)
    
    boton2 = Button(principal, text="Cerrar Sesion", bg="gray",
                command=cerrarSesion,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

    boton2.place(x=150,y=190)
    boton2.config(pady=10,width=10)
    
    
        
    principal.mainloop()