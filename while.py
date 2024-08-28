# dia = 0
# semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

# while dia < 7:
#     print ("hoy es: ",semana[dia])
#     dia += 1 
# ................
# contador = 1
# while contador <=10:
#    print(contador) 
#    contador += 1 #  contador = contador +1
   
   
#    contador = 1
#    while (contador <= 5):
#        contador = contador + 1
#        print ("interacion numero ", contador)

# contador = 0
# while contador < 15:
#     contador += 1
#     print ("Iteracion", contador)
#     if contador == 5:
#         break
#     print("fin")

# suma = 0
# while True:
#     numero = int(input("ingrese un numero(si quiere salir ingrese un numero negativo:)"))
#    if numero < 0:
#        break
#    suma += numero




#      print("la suma total es: ",suma)



# numero = 1
# while numero <= 100:
#     if numero % 7 == 0:
#         print("El primer número divisible por 7 es:", numero)
#         break
#     numero += 1

mayores = 0
menores = 0
contador = 0

# Bucle while para solicitar 10 notas
while contador < 10:
    nota = float(input(f"Ingrese la nota {contador+1}: "))
    
    if nota >= 7:
        mayores += 1
    else:
        menores += 1

    contador += 1

# Imprimir resultados
print(f"Alumnos con nota mayor o igual a 7: {mayores}")
print(f"Alumnos con nota menor a 7: {menores}")
