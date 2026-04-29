elif opcion == "1":
    # Ver todas las cuentas
    self.cliente.informacionCuentas()
    return True

elif opcion == "4":
    saldo = float(input("Saldo inicial: "))
    tipo = input("Tipo de cuenta: ")
    fecha = input("Fecha de creación: ")
    
    cuenta = Cuenta(saldo, tipo, fecha)
    self.cliente.agregarCuenta(cuenta)
    
    print("Cuenta agregada correctamente")
    return True

elif opcion == "5":
    self.cliente.informacionCuentas()
    
    indice = int(input("Número de cuenta a eliminar: ")) - 1
    self.cliente.eliminarCuenta(indice)
    return True
