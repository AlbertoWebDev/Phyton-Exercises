try:
    num = int(input("Introduce un número entero positivo y calcularé su factorial:"))
except ValueError:
    print("Error: Debes introducir un número entero válido.")
else:
    if num > 0:
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
        print("El factorial de ", num, " es: ", factorial)
    else:
        print("El número no es positivo o es 0. Inténtalo de nuevo.")