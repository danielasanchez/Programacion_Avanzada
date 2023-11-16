# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *
from tkinter import messagebox as MessageBox

def verificar(event):
    print(event.char)
    if len(input1.get())==0:
        input1.focus_set()
        
    
def enviar(event):
    print(event)
    print('Presionaste <Enter>')
    if input1.index("end")==0 or input2.index("end")==0:
        messagebox.showinfo("Error","Llena la informacion")
    else:
        messagebox.showinfo("Listo","Gracias por la informacion")


def obtener(event):
    print(f'El nombre es {input1.get()} {input2.get()}')

def click(mensaje):
    print(mensaje)
    
def ventanita(event):
    # revisar propiedades de bg, bd, etc.
    ventana = Toplevel(principal)
    ventana.title("Mi ventanita")
    ventana.geometry("180x80+500+300")
    # minsize(x,y)
    # maxsize(x,y)
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    # podemos agregar widgets
    label1 = Label(ventana, text="Soy una etiqueta")
    label1.pack()
    input1 = Entry(ventana, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green")
    input1.pack()
    
    
principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x450+400+200")
principal.config(bg="gray")


label2 = Label(principal,text="Nombre")
label2.pack()
label2.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))

input1 = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green")
input1.pack()


label3 = Label(principal,text="Apellido")
label3.pack()
label3.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))

input2 = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green")
input2.pack()
input2.bind("<Key>", verificar)
input2.bind('<Return>', enviar)


label3 = Label(principal,text="Dale clik")
label3.pack()
label3.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))
label3.bind("<Button>", obtener)


label4 = Label(principal,text="Tampoco le des clik")
label4.pack()
label4.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))
label4.bind("<Button>", ventanita)

texto="este mensaje no sirve para nada"

boton1 = Button(principal, text="Obtener", bg="gray",
                command=lambda : obtener(texto),
                activebackground="yellow",
                activeforeground="red",
                font=("Arial",16,"bold"),
                #state=DISABLED
                )

boton1.place(x=120,y=350)
boton1.config(pady=5,width=10)




principal.mainloop()

