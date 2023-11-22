# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:38:53 2023

@author: Daniela
"""



from tkinter import *
from tkinter import messagebox
from VentanaPrincipal import VentanaPrincipal

def VentanaLogin(usuarios):
    def loguear():
        print('verificando')
        if usuario.index("end")==0 or contra.index("end")==0:
            messagebox.showinfo("Error","Llena la informacion")
        else:
            #filtramos en una lista todos aquellos usuarios que coincidan con los ingresados
            #como estamos con un login, vamos a suponer que solo regresa uno.
            #por ese motivo mas adelante enviamos como parametro lista[0], para enviar al que
            #esta en la primer posicion.
            lista = list(filter(lambda u: u.user==usuario.get() and u.password==contra.get(),usuarios))
            
            if len(lista)==0:
                messagebox.showinfo("Error","Usuario o Contraseña incorrectos")
                usuario.focus_set()
                usuario.delete(0,END)
                contra.delete(0,END)
            else:
                print(f'Bienvenido (a) {lista[0].name}')
                loginWindow.destroy()
                #le enviamos al usuario identificado
                VentanaPrincipal(lista[0])
                
        
        
        
    loginWindow = Tk()
    loginWindow.title("Login")
    loginWindow.geometry("400x300+400+200")
    loginWindow.config(bg="gray")
    loginWindow.resizable(0,0)
  
    label1 = Label(loginWindow, text="Usuario:")
    label1.place(x=80,y=60)
    label1.config(width=10,bg="gray")
    
    usuario = Entry(loginWindow, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green")
    usuario.place(x=160,y=60)
    usuario.focus_set()
    
    label2 = Label(loginWindow, text="Contraseña:")
    label2.place(x=80,y=100)
    label2.config(width=10,bg="gray")
    
    # show = establecer el caracter a sustituir los caracteres
    contra = Entry(loginWindow, highlightthickness=4, highlightcolor="blue",
                   selectbackground="pink", selectforeground = "green",
                   show="*")
    
    contra.place(x=160,y=100)
    
    boton1 = Button(loginWindow, text="Entrar", bg="gray",
                    command=loguear,
                    activebackground="yellow",
                    activeforeground="red",
                    #state=DISABLED
                    )
    
    boton1.place(x=150,y=190)
    boton1.config(pady=10,width=10)
    loginWindow.mainloop()


