from cliente import Cliente
from cuenta import Cuenta

class Menu:
    def __init__(self):
        # Lista de clientes del sistema
        self.clientes = []

    def iniciar(self):
        while True:
            print("\n--- MENÚ ---")
            print("1. Crear cliente")
            print("2. Agregar cuenta")
            print("3. Ver cuentas")
            print("4. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre del cliente: ")
                cliente = Cliente(nombre)
                self.clientes.append(cliente)

            elif opcion == "2":
                nombre = input("Nombre del cliente: ")
                
                for cliente in self.clientes:
                    if cliente.nombre == nombre:
                        saldo = float(input("Saldo: "))
                        tipo = input("Tipo de cuenta: ")
                        
                        cuenta = Cuenta(saldo, tipo)
                        cliente.agregar_cuenta(cuenta)

            elif opcion == "3":
                nombre = input("Nombre del cliente: ")
                
                for cliente in self.clientes:
                    if cliente.nombre == nombre:
                        cliente.mostrar_cuentas()

            elif opcion == "4":
                break
