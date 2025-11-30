# Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.
cadena = input("Introduce una cadena de texto: ")
cadenaNueva = ""
for c in cadena:
    if c != " ":
        cadenaNueva = cadenaNueva + c
print("La cadena sin espacios:", cadenaNueva)