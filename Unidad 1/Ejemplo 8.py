"""
@author: Daniela Sanchez

"""

class Perro():
    vacunado=False
    def __init__(self,**kwargs):
        self.nombre=kwargs.get("nombre")
        self.raza=kwargs.get("raza")
        self.edad=kwargs.get("edad")
        print("Objeto Creado")
    def vacunar(self):
        self.vacunado=True

perrito1=Perro(nombre="Whisky",raza="Chihuahua",edad=11)
print(perrito1.nombre)



