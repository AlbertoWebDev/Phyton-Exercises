# Leer una cadena y contar cuántas vocales contiene.
cadena = input("Introduce una cadena de texto: ")
vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
contadorVocales = 0
for c in cadena:
    if c in vocales:
        contadorVocales = contadorVocales + 1
print("La cadena tiene ", contadorVocales, " vocales.")
