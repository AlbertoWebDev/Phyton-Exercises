try:
    n =int(input("Insertar la altura de la figura:"))
    indice_central = n // 2
    if n <= 0:
        raise ValueError
except ValueError:
    print("Error, la altura debe de ser numérica y mayor que Cero.")
else:

    for i in range(n):
        
        linea = ""
        
        for j in range(n):

            es_vertical = (j == 0) or (j == n - 1)
            
            es_diagonal_izquierda = (i == j) and (i <= indice_central)
            
            es_diagonal_derecha = (i + j == n - 1) and (i <= indice_central)

            if es_vertical or es_diagonal_izquierda or es_diagonal_derecha:
                caracter = "*"
            else:
                caracter = " "
                
            linea = linea + caracter
            
        print(linea)