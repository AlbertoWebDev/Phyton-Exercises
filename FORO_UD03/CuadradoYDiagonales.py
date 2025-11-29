try:
    n = int(input("Introduce la altura del cuadrado: "))
    if n < 0:
        print("Numero negativo no válido")
except ValueError:
    print("Introduce un número entero positivo.")
    exit()
else:
    for i in range(n):
        
        linea = ""
        
        for j in range(n):
            
            es_borde_horizontal = (i == 0) or (i == n - 1)
            
            es_borde_vertical = (j == 0) or (j == n - 1)
            
            es_diagonal_principal = (i == j)
            
            es_diagonal_secundaria = (i + j == n - 1)
        
            
            if es_borde_horizontal or es_borde_vertical or es_diagonal_principal or es_diagonal_secundaria:
                caracter = "*"
            else:
                caracter = " "
                
            linea = linea + caracter
            
        print(linea)