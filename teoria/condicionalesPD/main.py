from Cuenta import *
from Cliente import *
from Menu import *

# Creamos objetos
cuenta1 = Cuenta(1000.25, "Ahorro", "1/Enero/2005")
cliente1 = Cliente("Gustavo", "xboxcomunitry32@gmial.com", 22, cuenta1)

menu = Menu("BANCO CIENCIAS", cuenta1)

menu.darBienvenida()

#ciclo controlado por condicional (True/False)
continuar = True

while continuar:
    opcion = menu.despliegaMenu()
    continuar = menu.procesaOpcion(opcion)
