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
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        return input("Opción: ")

    def procesaOpcion(self, opcion):

        if opcion == "1":
            # Acceso correcto usando método
            print("Saldo actual:", self.cuenta.get_saldo())
            return True

        elif opcion == "2":
            cantidad = float(input("Cantidad: "))
            self.cuenta.depositar(cantidad)
            return True

        elif opcion == "3":
            cantidad = float(input("Cantidad: "))
            self.cuenta.retirar(cantidad)
            return True

        elif opcion == "4":
            return False

        else:
            print("Opción inválida")
            return True
