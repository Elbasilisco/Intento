class Cuenta_Bancaria:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def __str__(self):
        print(f"Titular: {self.titular}")
        print(f"Fondos: {self.cantidad}")
    def ingresar(self, monto):
        self.cantidad += monto
    def retirar(self, monto):
        self.cantidad -= monto

class Persona:
    def __init__(self):
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")