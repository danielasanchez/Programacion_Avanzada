"""
@author: Daniela Sanchez

"""

class Perro():
    nombre="Whisky"
    raza = "Chihuahua"
    edad = 11
    
    def __init__(self):
        print("Objeto Creado")
        
        
perrito1=Perro()
perrito2=Perro()

print(perrito1.nombre)
print(perrito2.nombre)