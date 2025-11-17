num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
print("La suma es:", suma)
resta = num1 - num2
print("La resta es:", resta)
multiplicacion = num1 * num2
print("La multiplicación es:", multiplicacion)

if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("Error: No se puede dividir entre cero.")
