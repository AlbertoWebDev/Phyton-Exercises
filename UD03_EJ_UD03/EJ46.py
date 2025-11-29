try:
    base = float(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))
except ValueError:
    print("Error, la base debe ser un número real y el exponente debe ser un entero.")
else:
    
    if exponente < 0:
        print("Error, el exponente debe ser un número entero positivo.")
    
    else:
        resultado = 1.0
        
        if exponente == 0:
            resultado = 1.0
            
        elif exponente == 1:
            resultado = base
            
        else:
            contador = 0
            resultado = 1.0
            
            while contador < exponente:
                resultado = resultado * base
                contador = contador + 1

        print("Base:", base)
        print("Exponente:", exponente)
        print("El resultado de la potencia es:", resultado)