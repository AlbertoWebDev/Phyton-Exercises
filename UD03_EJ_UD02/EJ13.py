try:
    altura=int(input("Insertar la altura de la escalera: "))
except ValueError:
    print("ERROR: Eres tonto ...")
else:
    base="1"
    for i in range(1, altura+1):
        print(base)
        
        base=base+str(i+1)