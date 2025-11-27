try:
    num = float(input("Introduce un número: "))
    
except ValueError:
    print("Error: Asegúrate de introducir un número válido.")

else:
    print("Número introducido: " + str(num))
    
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")