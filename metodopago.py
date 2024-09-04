class Paquete:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class MetodoPago:
    def __init__(self, nombre, descuento):
        self.nombre = nombre
        self.descuento = descuento

# Definición de paquetes
paquetes = [
    Paquete("Paquete 1", 100000),
    Paquete("Paquete 2", 200000),
    Paquete("Paquete 3", 300000)
]

# Definición de métodos de pago
metodos_pago = [
    MetodoPago("Efectivo", 0),
    MetodoPago("Tarjeta de crédito", 5),
    MetodoPago("PayPal", 10)
]

def mostrar_paquetes():
    print("Paquetes disponibles:")
    for i, paquete in enumerate(paquetes):
        print(f"{i+1}. {paquete.nombre} - ${paquete.precio}")

def mostrar_metodos_pago():
    print("Métodos de pago disponibles:")
    for i, metodo in enumerate(metodos_pago):
        print(f"{i+1}. {metodo.nombre} - {metodo.descuento}% de descuento")

def calcular_total(paquete, metodo_pago):
    return paquete.precio * (1 - metodo_pago.descuento / 100)

def main():
    print("Bienvenido a nuestro sistema de reservas")

    mostrar_paquetes()
    paquete_seleccionado = int(input("Seleccione un paquete: ")) - 1
    paquete = paquetes[paquete_seleccionado]

    mostrar_metodos_pago()
    metodo_pago_seleccionado = int(input("Seleccione un método de pago: ")) - 1
    metodo_pago = metodos_pago[metodo_pago_seleccionado]

    total = calcular_total(paquete, metodo_pago)
    print(f"Total a pagar: ${total}")

    pago = input("Desea realizar el pago (sí/no): ")
    if pago.lower() == "sí":
        print("Pago realizado con éxito")
        print("¡Gracias por tu compra! Esperamos que disfrutes de tu paquete.")
    else:
        print("Pago cancelado")

if __name__ == "__main__":
    main()






