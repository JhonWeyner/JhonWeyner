horas=float(input("ingrese el numero de horas que utilizo en el parqueadero"))
horascompletas = int(horas)+ 1 if horas % 1 !=0 else int (horas)

tarifahora = 1000
costototal = horascompletas * tarifahora
print (+ "el costo total es: $ {costototal} ")