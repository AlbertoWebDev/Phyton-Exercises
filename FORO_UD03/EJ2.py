try:
    altura=int(input("Insertar la altura de la figura:"))
    if altura<=0:
        raise ValueError
except ValueError:
    print("ERROR: La altura debe de ser numérica y mayor que Cero.")
else:
    print("----------------------------------------------------------------------------------------------")
    # Cabecera de la figura
    print("4")
    
    # Cuerpo de la figura
    for i in range(1,altura-1):
        print("4 ",end="")
        print("  "*(i-1),end="")
        print("4")
    
    # Base de la figura
    print("4 "*altura)