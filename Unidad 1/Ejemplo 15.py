"""
@author: Daniela Sanchez

"""

class Persona():
    def __init__(self,nombre,fechanacimiento):
        self.nombre=nombre
        self.fechanacimiento=fechanacimiento
        print("Objeto creado")
    def metodo1(self):
        pass

class Alumno(Persona):
    def __init__(self,nombre,fechanacimiento,carrera,calificaciones):
        super().__init__(nombre,fechanacimiento)
        self.carrera=carrera
        self.calificaciones=calificaciones
        print("Objeto alumno creado")
    def metodo2(self):
        pass

class Empleado(Persona):
    def __init__(self,nombre,fechanacimiento,puesto,sueldo):
        super().__init__(nombre,fechanacimiento)
        self.puesto=puesto
        self.sueldo=sueldo
        print("Objeto empleado creado")
    def metodo3(self):
        pass

persona1=Persona("Luis Gómez","02/03/2005")
alumno1=Alumno("Juan Peréz","09/22/2005","Inteligencia de Negocios",[100,97,95])
empleado1=Empleado("Carlos Fernández","01/07/2005","Coordinador",1500)






