try:
    base = float(input("introduce la base: "))
    exponente = float(input("introduce el exponente: "))

except ValueError:
    print("error: asegúrate de introducir solo números válidos.")

else:
    
    if exponente > 0:
        resultado = base ** exponente
        print("el exponente es positivo.")
        print("el resultado es: " + str(resultado))

    elif exponente == 0:
        resultado = 1.0
        print("el exponente es cero.")
        print("el resultado es: " + str(resultado))

    else:
        
        if base == 0:
            print("error: cero elevado a un exponente negativo es indefinido.")
        else:
            exponente_positivo = -exponente
            potencia_positiva = base ** exponente_positivo
            
            resultado = 1.0 / potencia_positiva
            
            print("el exponente es negativo.")
            print("el resultado es: 1 dividido por la potencia con exponente positivo.")
            print("el resultado es: " + str(resultado))