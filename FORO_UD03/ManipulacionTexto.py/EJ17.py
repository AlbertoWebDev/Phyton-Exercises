cadena_original = input("Introduce una cadena de texto: ")
cadena_caracteres_repetidos = ""
caracteres_ya_revisados = ""

for i in range(len(cadena_original)):
    caracter_actual = cadena_original[i]
    contador = 0

    if caracter_actual in caracteres_ya_revisados:
        continue

    for c in cadena_original:
        if c == caracter_actual:
            contador = contador + 1

    if contador > 1:
        cadena_caracteres_repetidos = cadena_caracteres_repetidos + caracter_actual
        
    caracteres_ya_revisados = caracteres_ya_revisados + caracter_actual

print(f"Cadena original: {cadena_original}")
print(f"Caracteres que se repiten: {cadena_caracteres_repetidos}")
