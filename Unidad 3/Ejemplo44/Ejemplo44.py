# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:38:53 2023

@author: Daniela
"""

from VentanaLogin import VentanaLogin


class Usuario():
    def __init__(self, name, user, password):
        self.name=name
        self.user=user
        self.password=password
        
# Defino los usuarios que si pueden tener acceso      
user1 = Usuario("Daniela Sánchez","Daniela","123")
user2 = Usuario("El administrador","admin","123")     

usuarios=[user1,user2]#usuarios permitidos en el login


#usar un user y password creados
def main():
    VentanaLogin(usuarios)
    
    
if __name__ == '__main__':
    main()