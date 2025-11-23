resultado = 1
try:
    num1 = int(input("introduce el valor base: "))
    num2 = int(input("introduce el valor exponente: "))
except ValueError:
    print("ERROR: Solo válidos números enteros.")
else:
    for i in range(num2):
        resultado = resultado * num1
print("El resultado de " + str(num1) + " elevado a " + str(num2) + " es: " + str(resultado))