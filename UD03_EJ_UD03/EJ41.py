print("Introduce números hasta que llegues a 5.")
numPositivos = 0
numNegativos = 0
numCero = 0
contadorNumeros = 0
num = None

while True:
    if contadorNumeros == 5:
        print("\nFin del bucle. Has llegado a 5 números.")
        break
    try:
        num = int(input("Introduce un número entero: "))
    except ValueError:
        print("No has introducido un número íntegro")
        continue
    else:
        contadorNumeros = contadorNumeros + 1
        if num == 0:
            numCero = numCero + 1
        elif num > 0:
            numPositivos = numPositivos + 1
        elif num < 0:
            numNegativos = numNegativos + 1

print("De los 5 números introducidos, ", numPositivos, " han sido positivos, ", numNegativos, " han sido negativos y ", numCero, " han sido 0.")

