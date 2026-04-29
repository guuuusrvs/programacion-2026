from Cuenta import *

class Cliente:
    def __init__(self, nombre, mail, edad, cuenta):

        self.nombre = nombre 
        self.mail = mail
        self.edad = edad

        self.cuenta = cuenta  

    def __str__(self):
        return f"Nombre::{self.nombre}  ::Mail::{self.mail}  ::Edad::{self.edad} ::Cuenta:: {self.cuenta}"
