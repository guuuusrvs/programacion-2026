class Cuenta:
    def __init__(self, saldo, tipo, fechaCreacion):
        self.saldo = saldo
        self.tipo = tipo
        self.fechaCreacion = fechaCreacion

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        else:
            print("Error: la cantidad debe ser mayor a 0")
            return False

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Error: fondos insuficientes")
            return False

        elif cantidad > 0:
            self.saldo -= cantidad
            return True

        else:
            print("Error: la cantidad debe ser mayor a 0")
            return False

    def __str__(self):
        return f"Saldo::{self.saldo} ::Tipo::{self.tipo} ::Fecha::{self.fechaCreacion}"
