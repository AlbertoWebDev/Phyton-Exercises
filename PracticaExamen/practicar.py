try:
    n = int(input("Introduce la altura de la figura: "))
    if n < 0:
        print("Numero negativo no válido")
except ValueError:
    print("Introduce un número entero positivo.")
    exit()
else:
    for i in range(n):
        lineas = ""
        for j in range(n, i + 1):
            lineas = lineas + "*"
        print(lineas)