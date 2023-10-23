# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

def obtener():
    #obtener la informacion
    valor = input1.get()
    print("el usuario capturado es: ",valor)
    #inicio,fin
    input1.delete(0,END)
    

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

label1 = Label(principal, text="Usuario:")
label1.place(x=80,y=60)
label1.config(width=10,bg="gray")

input1 = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green")
input1.place(x=160,y=60)



boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=170,y=150)
boton1.config(pady=10,width=10)


principal.mainloop()

