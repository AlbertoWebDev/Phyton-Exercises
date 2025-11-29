try:
    numero = int(input("Introduce el número entero para el cual quieres la tabla: "))
except ValueError:
    print("ERROR: Debes introducir un número entero válido.")
else:
    
    print("\nTabla de multiplicar del", numero, ":")

    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)