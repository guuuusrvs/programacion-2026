from Cuenta import *

class Menu:

    def __init__(self, mensaje, cuenta):
        self.mensajeBienvenida = mensaje
        self.cuenta = cuenta

    def darBienvenida(self):
        print("=" * 50)
        print(self.mensajeBienvenida)
        print("=" * 50)

    def despliegaMenu(self):
        print("-" * 50)
        print('Selecciona una opción:')
        print('1. Información de cuenta')
        print('2. Depositar')
        print('3. Retirar')
        print('4. Salir')
        print("-" * 50)
        return input("Elige una opción: ")

    def procesaOpcion(self, opcion):

        if opcion == '1':
            print('----- INFORMACIÓN -----')
            
            print(self.cuenta)
            return True
        
        elif opcion == "2":
            cantidad = float(input("Cantidad a depositar: "))
            
            if self.cuenta.depositar(cantidad):
                print(f"Nuevo saldo: {self.cuenta.saldo}")
            else:
                print("Error en el depósito")
            return True
            
        elif opcion == "3":
            cantidad = float(input("Cantidad a retirar: "))
            
            if self.cuenta.retirar(cantidad):
                print(f"Nuevo saldo: {self.cuenta.saldo}")
            else:
                print("Error en el retiro")
            return True
            
        elif opcion == "4":
            print("Sesión finalizada.")
            return False
        
        else:
            print("Opción inválida.")
            return True
