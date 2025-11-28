try:
    num1 = float(input("Introduce el dividendo (primer número): "))
    num2 = float(input("Introduce el divisor (segundo número): "))
    
except ValueError:
    print("Error: Asegúrate de introducir solo números válidos.")

else:
    
    if num2 == 0:
        print("Aviso: La división por cero es indefinida.")
        print("No se puede realizar la división entre " + str(num1) + " y 0.")
    else:
        division = num1 / num2
        
        print("El resultado de dividir " + str(num1) + " entre " + str(num2) + " es: " + str(division))