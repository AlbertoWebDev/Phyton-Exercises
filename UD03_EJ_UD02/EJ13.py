try:
    altura=int(input("Insertar la altura de la escalera: "))
except ValueError:
    print("ERROR: Valor no valido.")
else:
    if altura <= 0:
        print("ERROR: La altura debe ser un número positivo.")
    else:
        base="1"
        for i in range(1, altura+1):
            print(base)
        
            base=base+str(i+1)