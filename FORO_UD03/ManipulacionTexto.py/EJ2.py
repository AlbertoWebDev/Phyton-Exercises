# Concatenar caracteres o cadenas utilizando el operador + para formar nuevas cadenas.
cadena = input("Introduce una cadena de texto: ")
nuevaCadena = ""
for caracter in cadena:
    nuevaCadena += caracter + "-"
print("Cadena modificada: ", nuevaCadena)