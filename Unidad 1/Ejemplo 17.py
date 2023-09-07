from abc import ABC, abstractmethod
#Abstract Base Classes
class Persona(ABC):
    def __init__(self,nombre,fechanacimiento):
        self.nombre=nombre
        self.fechanacimiento=fechanacimiento
        print("Objeto creado")
    @abstractmethod
    def metodo(self):
        print("Hola desde Persona")

class Alumno(Persona):
    def __init__(self,nombre,fechanacimiento,carrera,calificaciones):
        super().__init__(nombre,fechanacimiento)
        self.carrera=carrera
        self.calificaciones=calificaciones
        print("Objeto alumno creado")
    def metodo(self):
        print("Hola desde Alumno")

class Empleado(Persona):
    def __init__(self,nombre,fechanacimiento,puesto,sueldo):
        super().__init__(nombre,fechanacimiento)
        self.puesto=puesto
        self.sueldo=sueldo
        print("Objeto empleado creado")
    def metodo(self):
        print("Hola desde Empleado")

# persona1=Persona("Luis Gómez","02/03/2005")
alumno1=Alumno("Juan Peréz","09/22/2005","Inteligencia de Negocios",[100,97,95])
empleado1=Empleado("Carlos Fernández","01/07/2005","Coordinador",1500)
empleado1.metodo()
