try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
except ValueError:
    print("Error: Uno o ambos valores introducidos no son números válidos.")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = "Indefinida (División por cero)"
    print("Suma: " + str(suma))
    print("Resta: " + str(resta))
    print("Multiplicación: " + str(multiplicacion))
    print("División: " + str(division))