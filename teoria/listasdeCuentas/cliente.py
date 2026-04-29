from Cuenta import *

class Cliente:
    def __init__(self, nombre, mail, edad):
        self.nombre = nombre 
        self.mail = mail
        self.edad = edad
        
        self.cuentas = [] 

    def agregarCuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminarCuenta(self, indice):
      #eliminar por posicion
        if 0 <= indice < len(self.cuentas):
            cuenta_eliminada = self.cuentas.pop(indice)
            print("Cuenta eliminada:", cuenta_eliminada)
            return True
        else:
            print("Índice inválido")
            return False

    def informacionCuentas(self):
        print("--- Cantidad de cuentas:", len(self.cuentas), "---")
        
        if len(self.cuentas) == 0:
            print("No hay cuentas registradas.")
        else:
            for i, cuenta in enumerate(self.cuentas, 1):
                print(f"{i}. {cuenta}")

    def __str__(self):
        return f"Nombre::{self.nombre}\nMail::{self.mail}\nEdad::{self.edad}"
