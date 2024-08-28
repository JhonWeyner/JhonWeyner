def calcular_cobro(horas, precio_hora):
    cobro_total = horas * precio_hora
    if horas % 1 != 0:
        cobro_total += precio_hora
    return cobro_total

horas = float(input("Ingrese las horas de estacionamiento: "))
precio_hora = float(input("Ingrese el precio por hora: "))

cobro_total = calcular_cobro(horas, precio_hora)
print("El cobro total es:", cobro_total)

