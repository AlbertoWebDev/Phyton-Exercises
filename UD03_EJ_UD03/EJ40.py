print("Introduce números positivos enteros. Se mostrará la suma y la media cuando introduzcas un 0.")

suma = 0
cantidadNumeros = 0
num = None

while True:
    
    try:
        num_str = input("Introduce un número entero (0 para terminar): ")
        num = int(num_str)
    except ValueError:
        print("Error, introduce un número entero válido.")
        continue
    
    if num == 0:
        print("\nHas introducido un 0. Fin del programa.")
        break
        
    elif num < 0:
        print("Error, el número debe ser positivo. Por favor, introduce un número positivo o 0 para terminar.")
        continue 
        
    else:
        suma = suma + num
        cantidadNumeros = cantidadNumeros + 1
        print(">> Número", num, "añadido. Suma actual:", suma)

if cantidadNumeros > 0:
    media = suma / cantidadNumeros
    print("La suma de todos los números introducidos es:", suma)
    print("La media de todos los números introducidos es:", media)
else:
    print("No se introdujeron números positivos válidos para calcular la suma y la media.")
