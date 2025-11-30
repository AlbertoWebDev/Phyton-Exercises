try:
    n = int(input("Introduce la altura del borde punteado: "))
    indice_central = n // 2
    if n < 0:
        print("Numero negativo no válido")
except ValueError:
    print("Introduce un número entero positivo.")
    exit()
else:
    for i in range(n):
        
        linea = ""
        
        for j in range(n):

            es_borde = (i == 0) or (i == n - 1) or (j == 0) or (j == n - 1)
            
            es_cruz_central = (i == indice_central) or (j == indice_central)
            
            if es_borde:
                caracter = "."
                
            elif es_cruz_central:
                caracter = "*"
                
            else:
                caracter = " "
            linea = linea + caracter
            
        print(linea)