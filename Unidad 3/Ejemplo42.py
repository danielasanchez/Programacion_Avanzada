# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:07:39 2023

@author: Daniela
"""

from tkinter import *
from ventanitasEjemplo2 import ventanita1, ventanita2, ventanitaFiltro, ventanitaRegistro


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("580x480+300+200")
principal.config(bg="gray")


menuPrincipal = Menu(principal)

# tearoff = separar menu
menuOpciones1 = Menu(menuPrincipal, tearoff=0)
menuOpciones2 = Menu(menuPrincipal, tearoff=0)

menuOpciones1.add_command(label="opcion 1", command = lambda : ventanita1(principal))
menuOpciones1.add_command(label="opcion 2", command = lambda : ventanita2(principal))
menuOpciones1.add_separator()
menuOpciones1.add_command(label="Cerrar", command=principal.destroy)

menuOpciones2.add_command(label="Registrar", command = lambda : ventanitaRegistro(principal))
menuOpciones2.add_command(label="Clases", command = lambda : ventanitaFiltro(principal))


menuPrincipal.add_cascade(label="Unidad 1", menu=menuOpciones1)
menuPrincipal.add_cascade(label="Unidad 2", menu=menuOpciones2)


principal.config(menu=menuPrincipal)


principal.mainloop()

