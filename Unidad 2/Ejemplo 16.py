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

archivo = open('MisPerritos.pckl','wb')
pickle.dump(perro,archivo)
archivo.close()

archivo = open('MisPerritos.pckl','rb')
objeto = pickle.load(archivo)
print(objeto.nombre)
