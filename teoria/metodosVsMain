#clases.py

#se dan los atributos 
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

#se muestra la informacion del producto
    def mostrar_producto(self):
        print("Producto:", self.nombre)
        print("Precio: $", self.precio)
        print("Stock disponible:", self.stock)

#se realiza la compra
    def comprar(self, cantidad):
        if cantidad <= self.stock:
            total = cantidad * self.precio
            self.stock = self.stock - cantidad
            print("Compra realizada con éxito")
            print("Total a pagar: $", total)
        if cantidad > self.stock:
            print("No hay suficiente stock disponible")
