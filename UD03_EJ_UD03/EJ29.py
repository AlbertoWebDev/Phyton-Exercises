try:
    a = float(input("introduce la longitud del lado a: "))
    b = float(input("introduce la longitud del lado b: "))
    c = float(input("introduce la longitud del lado c: "))
    
    if a <= 0 or b <= 0 or c <= 0:
        print("error: las longitudes de los lados deben ser mayores que cero.")
        a = None 

except ValueError:
    print("error: asegúrate de introducir solo números válidos.")

else:
    if a is not None:

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            print("no se puede formar un triángulo con estas longitudes.")
            
        else:
            lados = [a, b, c]
            lados.sort()
            
            x = lados[0]
            y = lados[1]
            z = lados[2]
            
            pitagoras = abs((x * x) + (y * y) - (z * z)) < 0.0001
            
            if a == b and b == c:
                print("el triángulo es equilátero.")
                
            elif pitagoras:
                print("el triángulo es rectángulo.")
                
            elif a == b or a == c or b == c:
                print("el triángulo es isósceles.")

            else:
                print("el triángulo es escaleno.")