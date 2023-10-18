# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("400x300+400+200")
principal.config(bg="gray")

label1 = Label(principal, text="Usuario:")
label1.place(x=80,y=60)
label1.config(width=10,bg="gray")

input1 = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green")
input1.place(x=160,y=60)


label2 = Label(principal, text="Contraseña:")
label2.place(x=80,y=100)
label2.config(width=10,bg="gray")

# show = establecer el caracter a sustituir los caracteres
input2 = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               show="*")

input2.place(x=160,y=100)

principal.mainloop()

