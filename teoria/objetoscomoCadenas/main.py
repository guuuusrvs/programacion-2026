from Cuenta import *
from Cliente import *
from Menu import *

cuenta1 = Cuenta(1000.18, 'Ahorro', '1/Enero/2005')

#cliente_cuenta
cliente1 = Cliente("Gustavo", "gustavorvs_14@ciencias.unam.mx", 20, cuenta1)

menu = Menu("BANCO CIENCIAS", cuenta1)

menu.darBienvenida()

continuar = True
while continuar:
    opcion = menu.despliegaMenu()
    continuar = menu.procesaOpcion(opcion)
