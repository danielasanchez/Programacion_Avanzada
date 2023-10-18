# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:48:54 2023

@author: Daniela Sánchez
"""

from tkinter import *

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("800x500+400+200")

label1= Label(principal,text="Hola mundo desde una etiqueta",
              font=("Arial",12,"bold","underline"),
              fg="blue",bg="green",height=4, width=40,
              bd=5,relief="ridge",
              wraplength=200,justify=CENTER)

label1.grid(row=0,column=0)

label2= Label(principal,text="Hola mundo desde otra etiqueta",
              font=("Arial",12,"bold","underline"),
              fg="blue",bg="green",height=4, width=40,
              bd=5,relief="ridge",
              wraplength=200,justify=CENTER)

label2.grid(row=1,column=1)

principal.mainloop()