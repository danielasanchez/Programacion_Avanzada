# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#MessageBox

from tkinter import *
from tkinter import messagebox as MessageBox

def ventanita():
    MessageBox.showinfo("Hola!", "Hola mundo") 
    # showwarning
    # showerror
    # askquestion
    # askokccancel
    # askopenfile
    # asksaveasfile
    
    

    
principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


boton1 = Button(principal, text="ver", bg="gray",
                command=ventanita,
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.pack()#place(x=150,y=190)
boton1.config(pady=10,width=10)


principal.mainloop()


