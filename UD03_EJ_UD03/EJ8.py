try:
    sueldoBase = int(input("¿Cuál es el sueldo base del vendedor?"))
    venta = int(input("¿Cuánto gana por cada venta?"))
except ValueError:
    print("Alguno de los valores introducidos no es válido. Introduce números enteros.")
else:
    if sueldoBase or venta <= 0:
        print("Los valores no pueden ser negativos o 0.")
    else:
        comision = sueldoBase * 0.10
        sueldoFinal = sueldoBase + comision
        print("El sueldo final del vendedor, aplicándole su 10%, será: " + sueldoFinal)
        
        
