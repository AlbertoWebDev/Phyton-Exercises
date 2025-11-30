# Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).
cadena = input("Introduce una cadena de texto: ")
nuevaCadena = ""
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
for c in cadena:
    if c not in vocales:
        nuevaCadena = nuevaCadena + c
    else:
        None
print("La cadena de texto con solo consonantes es: ", nuevaCadena)