"""
@author: Daniela Sanchez

"""
import pickle

class Perro():
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
        print("Objeto Creado")

perro = Perro("Whisky","Chihuahua")

cadena=pickle.dumps(perro)
print(cadena)

objeto = pickle.loads(cadena)
print(objeto)

