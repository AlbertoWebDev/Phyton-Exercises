try:
    n = int(input("Introduce la altura del rombo: "))
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
        
        linea = espacios_iniciales + "*"
        
        if i > 0:
            num_internos = 2 * i - 1
            espacios_internos = ""
            for k in range(num_internos):
                espacios_internos = espacios_internos + " "
                
            linea = linea + espacios_internos + "*"
            
        print(linea)

    for j in range(1, n):
        
        espacios_iniciales = ""
        for k in range(j):
            espacios_iniciales = espacios_iniciales + " "
        
        linea = espacios_iniciales + "*"
        
        num_internos = 2 * (n - 1 - j) - 1
        
        espacios_internos = ""
        for k in range(num_internos):
            espacios_internos = espacios_internos + " "
                
        linea = linea + espacios_internos + "*"
            
        print(linea)