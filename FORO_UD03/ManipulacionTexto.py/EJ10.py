# Leer una cadena y contar cuántos caracteres son letras mayúsculas.
cadena = input("Introduce una cadena de texto: ")
mayusculas = 'QWERTYUIOPÑLKJHGFDSAZXCVBNM'
contadorMayusculas = 0
for c in cadena:
    if c in mayusculas:
        contadorMayusculas = contadorMayusculas + 1
print("La cadena tiene ", contadorMayusculas, " letras mayúsculas.")
