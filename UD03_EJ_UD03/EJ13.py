#en Python se puede usar el operador ** para elevar un número a otro.
try:
    num = float(input("Introduce el número con el que aplicar las raíces: "))
except ValueError:
    print("No has introducido un número válido.")
else:
    raizCuadrada = num ** 0.5
    raizCubica = num ** (1/3)
    print("La raíz cuadrada es: ", raizCuadrada, " y la raíz cúbica es: " , raizCubica)