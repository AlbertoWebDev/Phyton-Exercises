# Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.
cadena = input("Introduce una cadena de texto: ")
contador = 0
for c in cadena:
    if '0' <= c <= '9':
        contador = contador + 1
print("La cadena tiene ", contador, " carácteres numéricos.")