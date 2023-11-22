# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:23:53 2023

@author: Daniela
"""
from tkinter import *

from tkinter import messagebox as MessageBox

class Usuario():
    def __init__(self, name, user, password):
        self.name=name
        self.user=user
        self.password=password
        
        
user1 = Usuario("Daniela Sánchez","Daniela","1234567")
user2 = Usuario("Brad Pitt","Brad","1234567")
user3 = Usuario("Ryan Reynolds","Ryan","1234567")
user4 = Usuario("admin","123","123")     

usuarios=[user1,user2,user3,user4]

# Show the window
def show(window):
    window.deiconify()
 
# Hide the window
def hide(window):
    window.withdraw()
    
    
    
def ventanita(encontrado):
    # revisar propiedades de bg, bd, etc.
    # principal.withdraw()
    ventana = Toplevel(principal)
    ventana.title("Mi ventanita")
    ventana.geometry("380x380+500+300")
    # minsize(x,y)
    # maxsize(x,y)
    ventana.resizable(0,0)
    # Deshabilita las otras ventanas (Modal)
    # ventana.grab_set()
    # aparece delante de la principal
    ventana.transient(master=principal)
    # podemos agregar widgets
    label1 = Label(ventana, text=encontrado.name)
    label1.pack()
    input1 = Entry(ventana, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green")
    input1.pack()
    
    principal.withdraw()
    ventana.deiconify()
    

    
def verificar():
    print('verificando')
    if usuario.index("end")==0 or contra.index("end")==0:
        messagebox.showinfo("Error","Llena la informacion")
    else:
        #filtramos en una lista todos aquellos usuarios que coincidan con los ingresados
        #como estamos con un login, vamos a suponer que solo regresa uno.
        lista = list(filter(lambda u: u.user==usuario.get() and u.password==contra.get(),usuarios))
        
        if len(lista)==0:
            messagebox.showinfo("Error","Usuario o Contraseña incorrectos")
        else:
            print(f'Bienvenido (a) {lista[0].name}')
            
            ventanita(lista[0])
            
            


    
    

principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("400x300+400+200")
principal.config(bg="gray")




# login = Toplevel()
# login.title("Mi primer ventana")
# login.geometry("400x300+400+200")
# login.config(bg="gray")
# login.transient(master=principal)

label1 = Label(principal, text="Usuario:")
label1.place(x=80,y=60)
label1.config(width=10,bg="gray")

usuario = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green")
usuario.place(x=160,y=60)


label2 = Label(principal, text="Contraseña:")
label2.place(x=80,y=100)
label2.config(width=10,bg="gray")

# show = establecer el caracter a sustituir los caracteres
contra = Entry(principal, highlightthickness=4, highlightcolor="blue",
               selectbackground="pink", selectforeground = "green",
               show="*")

contra.place(x=160,y=100)

boton1 = Button(principal, text="Entrar", bg="gray",
                command=lambda : verificar(),
                activebackground="yellow",
                activeforeground="red",
                #state=DISABLED
                )

boton1.place(x=150,y=190)
boton1.config(pady=10,width=10)




principal.mainloop()
