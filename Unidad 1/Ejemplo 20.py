"""
@author: Daniela Sanchez

"""

from enum import Enum

class Especialidades(Enum):
    Cardiologia = 700
    Dermatologia = 650
    Oftalmologia = 800
    Pediatria = 600


print(Especialidades.Cardiologia.value)

valor = "Pediatria"
print(Especialidades[valor].value)





