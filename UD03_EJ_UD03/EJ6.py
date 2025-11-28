try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))
    media = (num1 + num2 + num3) / 3
except ValueError:
    print("Algún valor introducido no ha sido válido.")
else:
    print("La media de los tres números es:", media)