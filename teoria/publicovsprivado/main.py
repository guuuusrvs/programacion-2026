from Cuenta import *
from Cliente import *
from Menu import *

cuenta1 = Cuenta(1000.17, "Ahorro", "1/Enero/2005")
cliente1 = Cliente("Gustavo", "xboxcomunity32@gmail.com", 20, cuenta1)

menu = Menu("BANCO CIENCIAS", cuenta1)

menu.darBienvenida()

continuar = True
while continuar:
    opcion = menu.despliegaMenu()
    continuar = menu.procesaOpcion(opcion)
