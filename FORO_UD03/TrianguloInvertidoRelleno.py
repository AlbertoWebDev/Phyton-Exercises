try:
    n =int(input("Insertar la altura de la figura:"))
    indice_central = n // 2
    if n <= 0:
        raise ValueError
except ValueError:
    print("Error, la altura debe de ser numérica y mayor que Cero.")
else:

    for i in range(n):
        
        espacios_iniciales = ""
        for k in range(i):
            espacios_iniciales = espacios_iniciales + " "
        
        linea = espacios_iniciales

        ancho_figura = 2 * (n - 1 - i) + 1
        
        for j in range(ancho_figura):

            if j == 0 or j == ancho_figura - 1:
                caracter = "*"
                
            else:
                
                if i % 2 == 1:
                    caracter = " "
                    
                else:
                    if j % 2 == 1:
                        caracter = "*"
                    else:
                        caracter = " "
                        
            linea = linea + caracter
            
        print(linea)