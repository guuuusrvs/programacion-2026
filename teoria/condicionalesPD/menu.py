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
        print("\n--- MENÚ ---")
        print("1. Ver cuenta")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        
        return input("Selecciona una opción: ")

    def procesaOpcion(self, opcion):

        if opcion == "1":
            print("\n--- INFORMACIÓN ---")
            print(self.cuenta)
            return True

        elif opcion == "2":
            cantidad = float(input("Cantidad a depositar: "))
            
            if self.cuenta.depositar(cantidad):
                print("Depósito exitoso")
            else:
                print("No se realizó el depósito")
            return True

        elif opcion == "3":
            cantidad = float(input("Cantidad a retirar: "))
            
            if self.cuenta.retirar(cantidad):
                print("Retiro exitoso")
            else:
                print("No se realizó el retiro")
            return True

        elif opcion == "4":
            print("Saliendo del sistema...")
            return False

        else:
            print("Opción inválida")
            return True
