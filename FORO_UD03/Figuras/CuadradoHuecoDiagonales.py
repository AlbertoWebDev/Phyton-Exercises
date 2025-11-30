try:
    n = int(input("Introduce el valor de n: "))
    
except ValueError:
    print("Por favor, introduce un número entero válido.")
    exit()
else: 
    for i in range(n):
        
        linea = ""
        
        for j in range(n):
            
            es_borde_exterior = (i == 0) or (i == n - 1) or (j == 0) or (j == n - 1)
            
            es_diagonal = (i == j) or (i + j == n - 1)
            
            es_asterisco_diseno_base = es_borde_exterior or es_diagonal
                        
            limite_min = 2
            limite_max = 6
            
            esta_en_area_hueca = (i > limite_min) and (i < limite_max) and (j > limite_min) and (j < limite_max)
            
            if esta_en_area_hueca and not es_asterisco_diseno_base:
                caracter = " "
            elif es_asterisco_diseno_base:
                caracter = "*"
            else:
                caracter = " "
                
            linea = linea + caracter
            
        print(linea)