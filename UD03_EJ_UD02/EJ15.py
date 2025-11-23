try:
    altura = int(input("Introduce la altura de la pirámide invertida: "))      
except ValueError:
    print("ERROR: Solo válidos números enteros positivos.")
        
else:      
    for i in range(altura, 0, -1):
        for j in range(0, altura - i):
            print(" ", end="")
        for k in range(1, 2 * i):
            print("*", end="")
        print("")
