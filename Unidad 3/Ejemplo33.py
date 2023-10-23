# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#Message

from tkinter import *


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

mensaje1 = Message(principal,text= "Lorem ipsum dolor sit amet, consectetur adipiscing elit")
mensaje1.pack()


principal.mainloop()

