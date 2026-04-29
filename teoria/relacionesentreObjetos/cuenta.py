class Cuenta:
    # Se crea una cuenta con sus datos básicos
    def __init__(self, saldo, tipo):

        self.saldo = saldo

        self.tipo = tipo

    def mostrar_info(self):
        print("Tipo:", self.tipo)
        print("Saldo:", self.saldo)
