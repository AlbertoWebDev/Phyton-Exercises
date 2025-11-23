try:
    altura = int(input("Introduce la altura de la escalera de números: "))
except ValueError:
    print("ERROR: Valor no valido.")
else:
    if altura <= 0:
        print("ERROR: La altura debe ser un número positivo.")
    else:
        for i in range(1, altura + 1):
            print(str(i) * i)
