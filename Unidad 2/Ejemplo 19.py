"""
@author: Daniela Sanchez

"""
import pickle

class Perro():
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
        print("Objeto Creado")
        
perros = []

nombres = ["Whisky", "Akira", "Tequila", "Ron"]
razas = ["Chihuahua", "Boxer", "Chihuahua", "Chihuahua"]

for n,r in zip(nombres,razas):
    p=Perro(n,r)
    perros.append(p)

print("Serializacion")

cadenas=pickle.dumps(perros)
print(cadenas)

