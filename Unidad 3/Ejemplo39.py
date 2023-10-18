# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#Menubutton

from tkinter import *

def activado():
    print("menu activado")
    
principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


menuboton = Menubutton(principal,text="Clase")
menuboton.place(x=10,y=10)


# tearoff = separar menu
menuOpciones1 = Menu(menuboton, tearoff=0, bg="pink",fg="blue",
                     activebackground="gray", activeborderwidth=10, 
                     activeforeground="pink", postcommand=activado)

menuOpciones1.add_command(label="Padre", state= DISABLED)
menuOpciones1.add_command(label="Hija")
menuOpciones1.add_separator()
menuOpciones1.add_command(label="Cerrar", command=principal.destroy)

menuboton["menu"]=menuOpciones1









principal.mainloop()

