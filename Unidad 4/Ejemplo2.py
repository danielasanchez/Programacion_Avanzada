# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:14:37 2023

@author: Daniela
"""

# Funciones de orden superior
def sumar(n1,n2):
    return n1+n2

def restar(n1,n2):
    return n1-n2

def dividir(n1,n2):
    return n1/n2

def multiplicar(n1,n2):
    return n1*n2


def operacion(numero1,numero2,funcion):
    return funcion(numero1,numero2)

resultado=operacion(10,3,sumar)
print(resultado)

