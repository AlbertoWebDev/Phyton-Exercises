try:
    altura=int(input("Insertar la altura de la figura:"))
    if altura<=0:
        raise ValueError
except ValueError:
    print("Error, la altura debe de ser numérica y mayor que Cero.")
else:
    print("4")
    
    for i in range(1,altura-1):
        print("4 ",end="")
        print("  "*(i-1),end="")
        print("4")
    
    print("4 "*altura)