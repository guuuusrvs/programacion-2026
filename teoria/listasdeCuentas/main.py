cliente1 = Cliente(Gustavo", "gustavorvs_14@ciencias.unam.mx", 20)

cuenta1 = Cuenta(1000.17, 'Ahorro', '1/Enero/2005')
cliente1.agregarCuenta(cuenta1)

menu = Menu("BANCO CIENCIAS", cliente1)
menu.darBienvenida()
menu.desplegarMenu()
