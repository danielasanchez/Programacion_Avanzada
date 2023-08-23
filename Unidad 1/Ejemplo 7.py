"""
@author: Daniela Sanchez

"""

class Perro():
    vacunado=False
    def __init__(self,nombre,raza,edad,*args):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.args=args
        print("Objeto Creado")
    def vacunar(self):
        self.vacunado=True

perrito1=Perro("Whisky","Chihuahua",11,"Nupec","Enojon","Dormir")
print(perrito1.args)


