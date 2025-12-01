"Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales"
"son iguales"
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
iguales = []

if num1 == num2 == num3:
    iguales = [num1, num2, num3]

elif num1 == num2:
    iguales = [num1, num2]

elif num1 == num3:
    iguales = [num1, num3]

elif num2 == num3:
    iguales = [num2, num3]

print("El número mayor es:", mayor)
print("El número menor es:", menor)

if iguales:
    print("Los números iguales son:", iguales)
else:
    print("No hay números iguales.")