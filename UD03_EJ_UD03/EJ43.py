print("Encontrar Números Pares en un Rango\n")
try:
    num_inicio = int(input("Introduce el primer número del rango (inicio): "))
    num_fin = int(input("Introduce el segundo número del rango (fin): "))
except ValueError:
    print("Error, debes introducir números enteros válidos.")
else:

    if num_inicio > num_fin:
        print("Aviso, el número de inicio era mayor que el de fin. Intercambiando el orden.")
  
        temp = num_inicio
        num_inicio = num_fin
        num_fin = temp
        
    print("\nBuscando números pares entre", num_inicio, "y", num_fin, "...")

    numeros_pares = []

    for numero in range(num_inicio, num_fin + 1):
        
        if numero % 2 == 0:
            numeros_pares.append(numero)

    if numeros_pares:
        print("\nLos números pares encontrados son:")
        print(numeros_pares)
    else:
        print("\nNo se encontraron números pares en ese rango.")