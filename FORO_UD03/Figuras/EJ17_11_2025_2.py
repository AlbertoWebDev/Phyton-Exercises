try:
    altura = int(input("Insertar la altura de la figura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error, la altura debe ser numérica y mayor que Cero.")
else:
    ancho = altura 
    
    for i in range(altura):
        linea = ""
        
        for j in range(ancho):
            
            if (i + j) % 2 == 0:
                linea += "*"
            else:
                linea += " "   
        print(linea)