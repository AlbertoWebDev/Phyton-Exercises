<<<<<<< HEAD
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2
print("La suma de" + str(num1) + " y " + str(num2) + " es: " + str(suma))
resta = num1 - num2
print("La resta de" + str(num1) + " y " + str(num2) + " es: " + str(resta))
multiplicacion = num1 * num2
print("La multiplicación de" + str(num1) + " y " + str(num2) + " es: " + str(multiplicacion))
if num2 != 0:
    division = num1 / num2
    print("La división de" + str(num1) + " y " + str(num2) + " es: " + str(division))
else:
    print("No se puede dividir por cero.")
=======
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
>>>>>>> 87418b80ae9cf92778beaaf2634274445ade0de7
