# Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.
cadena = input("Introduce una cadena de texto: ")
cadenaInversa = ""
for c in cadena:
    cadenaInversa = c + cadenaInversa
print("La cadena invertida es: ", cadenaInversa)