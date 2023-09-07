"""
@author: Daniela Sanchez

"""

class Perro():
    def __init__(self,nombre, raza, edad):
        self.__nombre=nombre
        self.__raza=raza
        self.__edad=edad
        print("Objeto Creado")
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,value):
        self.__nombre=value

perrito1=Perro("Whisky","Chihuahua",11)
print(perrito1.get_nombre())

perrito1.set_nombre("Tequila")
print(perrito1.get_nombre())






