class Cuenta:
    def __init__(self, saldo, tipo, fechaCreacion):
        self.__saldo = saldo
        self.__tipo = tipo
        self.__fechaCreacion = fechaCreacion

    def getSaldo(self):
        return self.__saldo
      
    def getTipo(self):
        return self.__tipo
      
    def getFechaCreacion(self):
        return self.__fechaCreacion

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        else:
            print('Cantidad inválida')
            return False

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print('Fondos insuficientes')
            return False
        elif cantidad > 0:
            self.__saldo -= cantidad
            return True
        else:
            print('Cantidad inválida')
            return False

    def __str__(self):
        return f"Saldo::{self.__saldo} ::Tipo::{self.__tipo} ::Fecha::{self.__fechaCreacion}"
