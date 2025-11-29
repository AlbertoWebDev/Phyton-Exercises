tam_bloque = 3
num_bloques_lado = 6 
n = tam_bloque * num_bloques_lado # Tamaño total de la matriz (18x18)

for i in range(n):
    
    linea = ""
    
    for j in range(n):
        
        bloque_fila = i // tam_bloque
        bloque_columna = j // tam_bloque
        
        if (bloque_fila + bloque_columna) % 2 == 0:
            caracter = "*"
        else:
            caracter = " "
            
        linea = linea + caracter
        
    print(linea)