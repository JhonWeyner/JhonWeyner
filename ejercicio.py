# Clase Paquete
class Paquete:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase MetodoPago
class MetodoPago:
    def __init__(self, nombre, descuento):
        self.nombre = nombre
        self.descuento = descuento

# Definición de paquetes
paquetes = [
    Paquete("Economía Plus", 850000),
    Paquete("Standard Plus", 1200000),
    Paquete("Lujo Plus", 2000000)
]

# Definición de métodos de pago
metodos_pago = [
    MetodoPago("Efectivo", 12),
    MetodoPago("Tarjeta Bancolombia", 15),
    MetodoPago("PSE", 10)
]

# Definición de hoteles
hoteles = [
    {"nombre": "Hotel 1", "precio": 200000},
    {"nombre": "Hotel 2", "precio": 350000},
    {"nombre": "Hotel 3", "precio": 500000}
]

# Definición de vuelos
vuelos = [
    {"nombre": "Avianca", "precio": 500000},
    {"nombre": "Copa Airlines", "precio": 550000},
    {"nombre": "LATAM", "precio": 600000}
]

# Variable para almacenar la compra
compra = []

# Función para mostrar paquetes
def mostrar_paquetes():
    print("Paquetes disponibles:")
    for i, paquete in enumerate(paquetes):
        print(f"{i+1}. {paquete.nombre} - ${paquete.precio}")

# Función para mostrar métodos de pago
def mostrar_metodos_pago():
    print("Métodos de pago disponibles:")
    for i, metodo in enumerate(metodos_pago):
        print(f"{i+1}. {metodo.nombre} - {metodo.descuento}% de descuento")

# Función para mostrar hoteles
def mostrar_hoteles():
    print("Hoteles disponibles:")
    for i, hotel in enumerate(hoteles):
        print(f"{i+1}. {hotel['nombre']} - ${hotel['precio']}")

# Función para mostrar vuelos
def mostrar_vuelos():
    print("Vuelos disponibles:")
    for i, vuelo in enumerate(vuelos):
        print(f"{i+1}. {vuelo['nombre']} - ${vuelo['precio']}")

# Función para agregar a la compra
def agregar_a_compra():
    global compra
    print("Seleccione una opción:")
    print("1. Paquete")
    print("2. Hotel")
    print("3. Vuelo")
    opcion = input("Opción: ")
    if opcion == "1":
        mostrar_paquetes()
        paquete_seleccionado = int(input("Seleccione un paquete: ")) - 1
        compra.append(paquetes[paquete_seleccionado])
    elif opcion == "2":
        mostrar_hoteles()
        hotel_seleccionado = int(input("Seleccione un hotel: ")) - 1
        compra.append(hoteles[hotel_seleccionado])
    elif opcion == "3":
        mostrar_vuelos()
        vuelo_seleccionado = int(input("Seleccione un vuelo: ")) - 1
        compra.append(vuelos[vuelo_seleccionado])

# Función para mostrar compra
def mostrar_compra():
    global compra
    print("Compra:")
    total = 0
    for i, item in enumerate(compra):
        if isinstance(item, Paquete):
            print(f"{i+1}. {item.nombre} - ${item.precio}")
            total += item.precio
        elif isinstance(item, dict):
            print(f"{i+1}. {item['nombre']} - ${item['precio']}")
            total += item['precio']
    print(f"Total: ${total}")

# Función para pagar
def pagar():
    global compra
    mostrar_compra()
    mostrar_metodos_pago()
    metodo_pago_seleccionado = int(input("Seleccione un método de pago: ")) - 1
    descuento = metodos_pago[metodo_pago_seleccionado].descuento
    total = 0
    for item in compra:
        if isinstance(item, Paquete):
            total += item.precio
        elif isinstance(item, dict):
            total += item['precio']
    total_con_descuento = total * (1 - descuento / 100)
    print(f"Total con descuento: ${total_con_descuento}")

# Menú principal
while True:
    print


