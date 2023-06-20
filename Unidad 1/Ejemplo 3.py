# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:37:09 2023

@author: Daniela
"""

class Perro():
    # nombre="Whisky"
    # raza = "Chihuahua"
    # edad = 11
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        print("Objeto Creado")

perrito1=Perro("Whisky","Chihuahua",11)
perrito2=Perro("Tequila","Chihuahua",10)

print(perrito1.nombre)
print(perrito2.nombre)
