num = int(input("Ingrese un número entero, o 0 si desea salir: "))
negativos = False
contador_negativos = 0
contador_positivos = 0
try:
    num = int(num)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
    exit()

if num == 0:
    print("No se ha leído ningún número.")
    
while num != 0:
    if num < 0:
        negativos = True
        contador_negativos += 1
    else:
        contador_positivos += 1
    num = int(input("Ingrese un número entero, o 0 si desea salir: "))
if negativos:
    print("Se han leído " + str(contador_negativos) + " números negativos.")
else:
    print("No se ha leído ningún número negativo.")
print("Se han leído " + str(contador_positivos) + " números positivos.")
