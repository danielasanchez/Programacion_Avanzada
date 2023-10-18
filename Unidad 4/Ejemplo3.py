# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:14:37 2023

@author: Daniela
"""

# Funciones de orden superior

def calcular_perro(edad):
    return edad*7
    
class Mascota():
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        print("Objeto Creado")
    def calcular(self,funcion):
        return funcion(self.edad)
        
    

perrito1=Mascota("Whisky","Chihuahua",11)
edad = perrito1.calcular(calcular_perro)
print("La edad humana de:", perrito1.nombre,"es:", edad)
