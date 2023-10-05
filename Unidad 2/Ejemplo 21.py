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

serializacion = json.dumps(perritos,indent=4)
type(serializacion) 
print(serializacion)

deserializacion = json.loads(serializacion)
type(deserializacion)
print(deserializacion)
