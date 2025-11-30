# Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.
cadena = input("Introduce una cadena de texto: ")
nuevaCadena = ""
vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
for c in cadena:
    if c in vocales:
        nuevaCadena = nuevaCadena + c + c
    else:
        nuevaCadena = nuevaCadena + c
print("La cadena con vocales duplicadas es: ", nuevaCadena)
