try:
    altura=int(input("Insertar la altura de la figura:"))
    if altura<=0:
        raise ValueError
except ValueError:
    print("Error, la altura debe de ser numérica y mayor que Cero.")
else:

    print(" " * altura, end = "")
    print("*")

    for i in range(1,altura+1):
        for j in range(i, altura):
            print(" ", end="")
        for k in range(1, 2):
            print("*",end="")
        for j in range(1,i):
            print(" ", end="")
        print("*")

    for i in range(1,altura):
        for j in range(1, i+1):
            print(" ", end="")
        for k in range(1, 2):
            print("*",end="")
        for j in range(i,altura-1):
            print(" ", end="")
        print("*")

    print(" "*altura,end="")
    print("*")