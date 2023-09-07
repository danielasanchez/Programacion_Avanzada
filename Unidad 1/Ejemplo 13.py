"""
@author: Daniela Sanchez

"""

class Trabajador():
    def __init__(self,numero,nombre,apellido):
        self.numero=numero
        self.nombre=nombre
        self.apellido=apellido
    def sueldo_semanal(self,*args):
        dias=args[0]
        pago=args[1]
        return dias*pago
    def sueldo_mensual(self,**kwargs):
        dias=kwargs.get("dias")
        pago=kwargs.get("pago")
        return (dias*pago)*4

Trabajador1=Trabajador(1234,"Juan","Perez")
sueldoSemanal=Trabajador1.sueldo_semanal(7,780)
sueldoMensual=Trabajador1.sueldo_mensual(dias=7,pago=780)

print("{} tiene un sueldo Semanal: {}".format(Trabajador1.nombre,sueldoSemanal))
print("{} tiene un sueldo Mensual: {}".format(Trabajador1.nombre,sueldoMensual))






