try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
except ValueError:
    print("Error: Asegúrate de introducir solo números válidos.")

else:
    if num1 > num2:
        print("El resultado es: El primer número (" + str(num1) + ") es mayor que el segundo (" + str(num2) + ").")
    elif num1 < num2:
        print("El resultado es: El primer número (" + str(num1) + ") es menor que el segundo (" + str(num2) + ").")
    else:
        print("El resultado es: Ambos números son iguales.")