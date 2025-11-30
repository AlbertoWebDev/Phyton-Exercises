# Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.
cadena = input("Introduce una cadena de texto: ")
caracter = input("Que caracter específico quieres verificar: ")
verificar = False
for n in cadena:
    if caracter in cadena:
        verificar = True
if verificar:
    print("El valor ", caracter, " existe en la cadena introducida.")
else:
    print("El valor ", caracter, " no existe en la cadena introducida.")
