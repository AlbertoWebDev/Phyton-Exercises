try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))
except ValueError:
    print("Error: Asegúrate de introducir solo números válidos.")
else:
    media = (num1 + num2 + num3) / 3.0
    print("Primer número: " + str(num1))
    print("Segundo número: " + str(num2))
    print("Tercer número: " + str(num3))
    print("La media es: " + str(media))