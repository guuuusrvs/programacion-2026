#menu.py

#crear objetos y llamar metodos
producto1 = Producto("Playera", 250, 10)
producto2 = Producto("Zapatillas", 500, 20)

opcion = 0

#opciones principales del menu
while opcion != 3:
    print("--- TIENDA ---")
    print("1. Mostrar productos")
    print("2. Comprar productos")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion: "))

#metodod para mostrar producto
    if opcion == 1:
        producto1.mostrar_producto()
        producto2.mostrar_producto()

  #pedir datos y correr
    if opcion == 2:
        print("¿Qué producto desea comprar?")
        print("1. Playera")
        print("2. Zapatillas")

        seleccion = int(input("Seleccione producto: "))
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))

        if seleccion == 1:
            producto1.comprar(cantidad)

        if seleccion == 2:
            producto2.comprar(cantidad)

print("Gracias por visitar la tienda")
