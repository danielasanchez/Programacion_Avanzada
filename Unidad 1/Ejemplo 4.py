"""
@author: Daniela Sanchez

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