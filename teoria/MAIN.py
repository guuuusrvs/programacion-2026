def main():
    # crear objetos
    producto1 = Producto("Playera", 250, 10)
    producto2 = Producto("Zapatillas", 500, 20)

    opcion = 0

    # menú principal
    while opcion != 3:
        print("\n--- TIENDA ---")
        print("1. Mostrar productos")
        print("2. Comprar productos")
        print("3. Salir")

        opcion = int(input("Ingrese una opción: "))

        # mostrar productos
        if opcion == 1:
            producto1.mostrar_producto()
            print("------------------")
            producto2.mostrar_producto()

        # comprar productos
        elif opcion == 2:
            print("\n¿Qué producto desea comprar?")
            print("1. Playera")
            print("2. Zapatillas")

            seleccion = int(input("Seleccione producto: "))
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))

            if seleccion == 1:
                producto1.comprar(cantidad)
            elif seleccion == 2:
                producto2.comprar(cantidad)
            else:
                print("Opción inválida")

        elif opcion == 3:
            print("Gracias por visitar la tienda")

        else:
            print("Opción no válida")

# punto de entrada
if __name__ == "__main__":
    main()
