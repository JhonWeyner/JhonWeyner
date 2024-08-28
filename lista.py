# frutas = ["manzana", "pera","uva","banano"]
# numero =[89,87,65,78,56]
# frutas.append("sandia")#para agregar un elemento
# frutas.insert(0, "papaya")#para agregar un elemento en una exposicion especifica de la lista 
# frutas.extend(["mango","kiwi","lulo"])#sirve para agregar multiple de elementos a la listas 
# frutas[8] = "limon" #editar un elemento de la lista ya que el primero era papaya y se eliminara y se agregara limon
# frutas.remove("papaya")#para remover un elemnto de la lista 
# del frutas [7] #para eliminar un elemento de la lista 
# del frutas [0:4]#eliminamos por rango
# frutas.clear() eliminar toda lista

# Escribe un programa en Python que solicite al usuario ingresar una lista de números enteros. Luego, el programa debe calcular e imprimir la suma de todos los números ingresados. El programa debe continuar solicitando números hasta que el usuario decida dejar de ingresar más.

# Requisitos:

# El programa debe permitir al usuario ingresar números uno por uno.
# Después de ingresar cada número, el usuario debe ser preguntado si desea agregar otro número.
# Si el usuario decide que no quiere agregar más números, el programa debe calcular y mostrar la suma total de los números ingresados.
numeros = []
while True:
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)
    continuar = input("¿Quiere agregar otro número? (si/no): ")
    if continuar.lower() == "no":
        break
suma_total = sum(numeros)
print(f"La suma total de los números ingresados es: {suma_total}")











# Escribe un programa en Python que permita al usuario crear una lista de compras. El programa debe solicitar al usuario que ingrese el nombre de los productos uno por uno y los agregue a la lista. Una vez que el usuario haya terminado de agregar productos, el programa debe imprimir la lista completa de compras en orden.

# Requisitos:

# El programa debe permitir al usuario ingresar productos hasta que decida detenerse.
# Después de ingresar cada producto, el usuario debe ser preguntado si desea agregar otro producto.
# Si el usuario decide que no quiere agregar más productos, el programa debe mostrar la lista completa de compras.

# lista = []
# while True:
#     producto = input("ingrese el producto a lista de compras")
    
#     lista.append (producto)
    
#     continuar = input("quiere agregar otro producto a la lista? (si / no): ")
    
#     if continuar == "no":
#          break
     
# print("N tu lista de compra es")

# for item in lista:p
#      print(f"-{item}")







# frutaseliminada = frutas.pop(1)

# print(frutas)
# print (frutaseliminada)


# for i in frutas:#imprimir
#     print(i) #de forma vertical



# print(frutas)