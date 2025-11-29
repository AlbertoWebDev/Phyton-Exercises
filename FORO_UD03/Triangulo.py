try:
    n = int(input("Introduce la altura del triángulo: "))
    if n < 0:
        print("Numero negativo no válido")
except ValueError:
    print("Introduce un número entero positivo.")
    exit()
else:
    for i in range (n):
        linea = ""
        for j in range(i + 1):
            linea = linea + "*" 
        print(linea)