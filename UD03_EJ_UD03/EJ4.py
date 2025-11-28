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