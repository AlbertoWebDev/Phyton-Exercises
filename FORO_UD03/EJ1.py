try:
    altura=int(input("Insertar la altura de la figura:"))
    if altura<=0:
        raise ValueError
except ValueError:
    print("ERROR: La altura debe de ser numérica y mayor que Cero.")
else:
    # Primer escalón de la Figura
    print(" "*altura,end="")
    print("*")
    # Parte 1 de la Figura
    for i in range(1,altura+1):
        for j in range(i, altura):
            print(" ", end="")
        for k in range(1, 2):
            print("*",end="")
        for j in range(1,i):
            print(" ", end="")
        print("*")
    # Parte 2 de la Figura    
    for i in range(1,altura):
        for j in range(1, i+1):
            print(" ", end="")
        for k in range(1, 2):
            print("*",end="")
        for j in range(i,altura-1):
            print(" ", end="")
        print("*")
    # Último escalón de la figura
    print(" "*altura,end="")
    print("*")