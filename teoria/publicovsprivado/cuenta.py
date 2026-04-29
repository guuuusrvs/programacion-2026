class Cuenta:
    def __init__(self, saldo, tipo, fechaCreacion):
        
        #atributo PRIVADO (no se debe modificar directamente)
        self.__saldo = saldo
        
        #atributo públicos
        self.tipo = tipo
        self.fechaCreacion = fechaCreacion

    def get_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        else:
            print("Error: cantidad inválida")
            return False

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Error: fondos insuficientes")
            return False
        elif cantidad > 0:
            self.__saldo -= cantidad
            return True
        else:
            print("Error: cantidad inválida")
            return False

    def __str__(self):
        return f"Saldo::{self.__saldo} ::Tipo::{self.tipo} ::Fecha::{self.fechaCreacion}"
