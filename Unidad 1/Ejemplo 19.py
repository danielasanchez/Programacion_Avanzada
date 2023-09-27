"""
@author: Daniela Sanchez

"""

from enum import Enum

class Dias(Enum):
    Lunes = "monday"
    Martes = "tuesday"
    Miercoles = "wednesday"
    Jueves = "thursday"
    Viernes = "friday"
    Sabado = "saturday"
    Domingo = "sunday"

print(Dias.Lunes.value)
print(Dias("wednesday"))
print(Dias['Martes'].value)

print(list(Dias))
