"""
@author: Daniela Sanchez

"""
import json
# JSON (acrónimo de JavaScript Object Notation, 'notación de objeto de JavaScript')

perritos = [
    {'nombre':'Whisky','raza':'Chihuahua','edad':'11'},
    {'nombre':'Akira','raza':'Boxer','edad':'5'},
    {'nombre':'Tequila','raza':'Chihuahua','edad':'10'},
    {'nombre':'Ron','raza':'Chihuahua','edad':'10'},
]

print("Crear archivo....")

archivo = open("archivo.json","w")

json.dump(perritos,archivo)
# with open("archivo.json","w") as archivo:
#     json.dump(Mis_perritos,archivo)

print("Leer archivo....")
Mis_perritos=[]

archivo = open("archivo.json","r")

perritos = json.load(archivo)
# with open("archivo.json","r") as archivo:
#     perritos = json.load(archivo)

for p in perritos:
    print(p['nombre'])
