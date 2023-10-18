# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#Menu

from tkinter import *

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
                     activeforeground="pink", postcommand=activado)

menuOpciones1.add_command(label="opcion 1", state= DISABLED)
menuOpciones1.add_command(label="opcion 2")
menuOpciones1.add_separator()
menuOpciones1.add_command(label="Cerrar", command=principal.destroy)


menuOpciones2 = Menu(menuPrincipal, tearoff=0)
menuOpciones2.add_command(label="opcion 1")
menuOpciones2.add_command(label="opcion 2")
menuOpciones2.add_command(label="opcion 3")

#seleccionar varias opciones
menuOpciones3 = Menu(menuPrincipal, tearoff=0)
menuOpciones3.add_checkbutton(label="Opcion 1")
menuOpciones3.add_checkbutton(label="Opcion 2")
menuOpciones3.add_checkbutton(label="Opcion 3")

#solo seleccionar una opcion del menu
menuOpciones4 = Menu(menuPrincipal, tearoff=0)
menuOpciones4.add_radiobutton(label="Opcion 1")
menuOpciones4.add_radiobutton(label="Opcion 2")
menuOpciones4.add_radiobutton(label="Opcion 3")

menuPrincipal.add_cascade(label="Opciones 1", menu=menuOpciones1)
menuPrincipal.add_cascade(label="Opciones 2", menu=menuOpciones2)
menuPrincipal.add_cascade(label="Opciones 3", menu=menuOpciones3)
menuPrincipal.add_cascade(label="Opciones 4", menu=menuOpciones4)



principal.config(menu=menuPrincipal)





principal.mainloop()

