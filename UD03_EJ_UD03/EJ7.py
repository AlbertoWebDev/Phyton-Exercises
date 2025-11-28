try:
    minutos = int(input("Ingrese los minutos que desea convertir: "))
except ValueError:
    print("Valor introducido no válido")
else:
    segundos = minutos * 60
    horas = minutos / 60
    print(str(minutos) + " minutos son " + str(segundos) + " segundos o " + str(horas) + " horas.")