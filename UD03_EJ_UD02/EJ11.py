try:
    num=int(input("Insertar el tamaño de la escalera: "))
except ValueError:
    print("ERROR: Valor no valido.")
else:
    variable="*"
    for i in range( 1,num+1 ):
        if( i==1 ):
           print(variable)
        else:
            variable = variable + "*"
            print(variable)