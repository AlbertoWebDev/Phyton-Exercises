try:
    dado = int(input("Ingresa la cara del dado que ha salido (1-6):"))
except ValueError:
    print("Error: Debes ingresar un número entero.")
else:
    if 1 <= dado <= 6:
        opuestos = ["uno","dos","tres","cuatro","cinco","seis"]
        if dado == 1:
            print("El opuesto es: ", opuestos[5])
        elif dado == 2:
            print("El opuesto es, ", opuestos[4])
        elif dado == 3:
            print("El opuesto es: ", opuestos[3])
        elif dado == 4:
            print("El opuesto es: ", opuestos[2])
        elif dado == 5:
            print("El opuesto es: ", opuestos[1])
        elif dado == 6:
            print("El opuesto es: ", opuestos[0])

    else:
        print("No has introducido un número entre 1 y 6.")