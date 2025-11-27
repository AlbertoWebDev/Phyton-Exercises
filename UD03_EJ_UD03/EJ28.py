try:
    num1 = float(input("introduce el primer número: "))
    num2 = float(input("introduce el segundo número: "))
    num3 = float(input("introduce el tercer número: "))

except ValueError:
    print("error: asegúrate de introducir solo números válidos.")

else:

    mayor = 0.0
    medio = 0.0
    menor = 0.0
    

    if num1 >= num2 and num1 >= num3:
        mayor = num1
        if num2 >= num3:
            medio = num2
            menor = num3
        else:
            medio = num3
            menor = num2
    
    elif num2 >= num1 and num2 >= num3:
        mayor = num2
        if num1 >= num3:
            medio = num1
            menor = num3
        else:
            medio = num3
            menor = num1
            
    else:
        mayor = num3
        if num1 >= num2:
            medio = num1
            menor = num2
        else:
            medio = num2
            menor = num1

    print("orden: " + str(mayor) + ", " + str(medio) + ", " + str(menor))