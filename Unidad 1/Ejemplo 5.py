"""
@author: Daniela Sanchez

"""

class Perro():
    vacunado=False

    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        print("Objeto Creado")
    def vacunar(self):
        vacunado=True

perrito1=Perro("Whisky","Chihuahua",11)
perrito1.vacunar()
print(perrito1.nombre)
perrito1.vacunar()
print(perrito1.vacunado)

