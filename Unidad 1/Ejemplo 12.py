"""
@author: Daniela Sanchez

"""

class Perro():
    vacunado=False
    def __init__(self,*args,**kwargs):
        self.nombre=kwargs.get("nombre")
        self.raza=kwargs.get("raza","Criollo")
        self.edad=kwargs.get("edad")
        self.vacunas=args
        print("Objeto Creado")
    def vacunar(self):
        self.vacunado=True

perrito1=Perro("Parvovirus","Rabia",nombre="Whisky",edad=11) 
print(perrito1.raza)
print(perrito1.vacunas)






