try:
    n = int(input("Introduce la altura de la reja: "))
    if n < 0:
        print("Numero negativo no válido")
except ValueError:
    print("Introduce un número entero positivo.")
    exit()
else:

    for i in range(n):
        
        espacios_iniciales = ""
        for k in range(n - 1 - i):
            espacios_iniciales = espacios_iniciales + " "
        
        linea = espacios_iniciales
            
        if i == n - 1:
            for j in range(2 * n - 1):
                linea = linea + "*"
        
        else:
            ancho_patron = 2 * i + 1
            
            for j in range(ancho_patron):
                
                if j == 0 or j == ancho_patron - 1:
                    linea = linea + "*"
                    
                else:
                    if i % 2 == 1:
                        if j % 2 == 1:
                            linea = linea + "*"
                        else:
                            linea = linea + " "
                    
                    elif i % 2 == 0:
                        linea = linea + " "
        
        print(linea)