num = int(input("Ingrese su número: "))
if 0 < num < 99999:
    if num < 10:
        print("El número tiene 1 cifra")
    elif num < 100:
        print("El número tiene 2 cifras")
    elif num < 1000:
        print("El número tiene 3 cifras")
    elif num < 10000:
        print("El número tiene 4 cifras")
    else:
        print("El número tiene 5 cifras")
else:
    print("El número no está entre 0 y 99999")
