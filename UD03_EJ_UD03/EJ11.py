try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
except ValueError:
    print("Por favor, introduce valores numéricos válidos.")
    exit()
else:
    if num1 == num2:
        print("Los números son iguales. No hay distancia entre ellos.")
        exit()
    else:
        distancia = abs(num1 - num2)
        print("La distancia entre ", num1, " y ", num2, " es: ", distancia)
