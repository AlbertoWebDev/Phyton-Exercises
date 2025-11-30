# Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).
cadena_original = input("Introduce una cadena para convertir a minusculas: ")
cadena_minusculas = ""

for caracter in cadena_original:
    valor = ord(caracter)

    if 'A' <= caracter <= 'Z':
        nuevo_valor = valor + 32
        caracter_convertido = chr(nuevo_valor)
        cadena_minusculas = cadena_minusculas + caracter_convertido
    else:
        cadena_minusculas = cadena_minusculas + caracter

print(f"Resultado en Minúsculas: {cadena_minusculas}")