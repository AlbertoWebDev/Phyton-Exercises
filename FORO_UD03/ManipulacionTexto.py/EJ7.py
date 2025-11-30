# Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.
cadena = input("Introduce una cadena de texto: ")
caracter = input("Que caracter quieres reemplazar?: ")
reemplazo = input("Por cual quieres reemplazarlo?: ")
cadenaModificada = ""
if len(reemplazo) != 1 or len(caracter) != 1:
    print("\nError, solo puedes introducir un caracter.")
else:
    for c in cadena:
            if c == caracter:
                cadenaModificada = cadenaModificada + reemplazo
            else:
                cadenaModificada = cadenaModificada + c
    print("Cadena original: ", cadena)
    print("Cadena modificada: ", cadenaModificada)