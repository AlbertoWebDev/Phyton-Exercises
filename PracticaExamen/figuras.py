try:
    altura=int(input("Insertar la altura de la figura: "))
    if altura<=0:
        raise ValueError
except ValueError:
    print("ERROR: La altura debe de ser numérica y mayor que Cero.")
else:
 
    # Parte 1 de la Figura
    for i in range(1,altura):

        if(i==1):

            print(" "*altura,end="")

            print("*")
        else:

            print(" "*(altura - i) + "*" + " "*(i - 1) + "*")



    # Parte 2 de la Figura
    for i in range(altura, 0, -1):
            
            print(" "*(altura - i) + "*" + " "*(i - 1) + "*")
        
    print(" "*altura,end="")

    print("*")