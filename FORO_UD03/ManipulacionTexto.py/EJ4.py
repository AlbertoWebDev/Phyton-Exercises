# Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).
cadena_original = "Python es divertido"
cadena_filtrada = ""
vocales = "aeiouAEIOU"

for caracter in cadena_original:
    if caracter not in vocales:
        cadena_filtrada = cadena_filtrada + caracter

print("Original:", cadena_original)
print("Filtrada:", cadena_filtrada)