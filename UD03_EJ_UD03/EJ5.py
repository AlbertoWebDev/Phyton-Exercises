<<<<<<< HEAD
F = float(input("Ingrese los grados a convertir: "))
C = (F - 32) * 5/9
print(str(F) + " grados Fahrenheit son " + str(C) + " grados Celsius.")
=======
try:
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit (F): "))
except ValueError:
    print("Error: El valor introducido no es un número válido.")
else:
    celsius = (fahrenheit - 32.0) * (5.0 / 9.0)
    print("\n--- Resultado de la Conversión ---")
    print("Temperatura en Fahrenheit: " + str(fahrenheit) + "°F")
    print("Temperatura en Celsius: " + str(celsius) + "°C")
>>>>>>> 87418b80ae9cf92778beaaf2634274445ade0de7
