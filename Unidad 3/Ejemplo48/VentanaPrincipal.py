# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:38:53 2023

@author: Daniela
"""
from tkinter import *
from VentanaProductos import VentanaProductos
from VentanaCompra import VentanaCompra
from VentanaHistorial import VentanaHistorial

def VentanaPrincipal():
    
    def activado():
        print("menu activado")
        
    principal = Tk()
    principal.title("Mi primer ventana")
    principal.geometry("380x280+400+200")
    principal.config(bg="gray")
    
    
    menuPrincipal = Menu(principal)
    
    # tearoff = separar menu
    menuOpciones1 = Menu(menuPrincipal, tearoff=0, bg="pink",fg="blue",
                         activebackground="gray", activeborderwidth=10, 
                         activeforeground="pink"#, postcommand=activado
                         )
    
    
    menuOpciones1.add_command(label="Comprar", command=lambda:VentanaCompra(principal))
    menuOpciones1.add_separator()
    menuOpciones1.add_command(label="Cerrar", command=principal.destroy)
    
    
    menuOpciones2 = Menu(menuPrincipal, tearoff=0)
    menuOpciones2.add_command(label="Papeleria", command=lambda:VentanaProductos(principal))

    #seleccionar varias opciones
    menuOpciones3 = Menu(menuPrincipal, tearoff=0)
    menuOpciones3.add_command(label="Compras", command=lambda:VentanaHistorial(principal))

    
    #solo seleccionar una opcion del menu
    menuOpciones4 = Menu(menuPrincipal, tearoff=0)
    menuOpciones4.add_radiobutton(label="Opcion 1")
    menuOpciones4.add_radiobutton(label="Opcion 2")
    menuOpciones4.add_radiobutton(label="Opcion 3")
    
    menuPrincipal.add_cascade(label="Opciones 1", menu=menuOpciones1)
    menuPrincipal.add_cascade(label="Productos", menu=menuOpciones2)
    menuPrincipal.add_cascade(label="Historial", menu=menuOpciones3)
    menuPrincipal.add_cascade(label="Opciones 4", menu=menuOpciones4)
    
    principal.config(menu=menuPrincipal)
    principal.mainloop()
    

VentanaPrincipal()