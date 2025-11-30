try:
    altura = int(input("Introduce la altura de la figura: "))
    if altura < 0:
        print("Numero negativo no válido")
except ValueError:
    print("Introduce un número entero positivo.")
    exit()
else:
    for i in range(altura):
        linea = ""
        for j in range(i + 1):
            linea = linea + "*"
        print(linea)