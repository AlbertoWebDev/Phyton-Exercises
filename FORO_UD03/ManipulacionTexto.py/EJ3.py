# Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.
cadena = input("Introduce una cadena de texto y mostraré cuantas letras s contiene: ")
contador = 0
for s in cadena:
    if s == "s" or s == "S":
        contador += 1
print("El número de veces que aparece la letra s es: ", contador)
