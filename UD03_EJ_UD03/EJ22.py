try:
    num = int(input("Introduce un número entero: "))
    
except ValueError:
    print("Error: Asegúrate de introducir un número entero válido.")

else:
    print("Número introducido: " + str(num))
    
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")