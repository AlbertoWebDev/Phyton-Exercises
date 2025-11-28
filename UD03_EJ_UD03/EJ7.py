try:
    minutos_totales = int(input("Introduce la cantidad de minutos: "))

    if minutos_totales < 0:
        print("Error: La cantidad de minutos debe ser un número positivo.")
    else:
        pass
except ValueError:
    print("Error: El valor introducido no es un número entero válido.")
else:
    horas = minutos_totales // 60

    minutos = minutos_totales % 60

    print("Minutos totales introducidos: " + str(minutos_totales))
    print("Corresponde a: " + str(horas) + " horas y " + str(minutos) + " minutos.")