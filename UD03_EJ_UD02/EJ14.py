try:
    # Pedimos la altura de la escalera
    altura=int(input("Intruce la altura de la pirámide: "))
    if altura<=0:
        raise ValueError
except ValueError:
    print("ERROR: solamente son validos los números enteros")
else:
    for i in range(1,altura+1):
        # Vamos a construir los espacios
        for j in range(i,altura):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print("")