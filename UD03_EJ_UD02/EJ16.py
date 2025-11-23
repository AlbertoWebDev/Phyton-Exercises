diezEncontrado = False
notas = int(input("Introduce una nota (0-10) o -1 para terminar el bucle: "))
while notas != -1:
    if notas == 10:
        diezEncontrado = True
    notas = int(input("Introduce una nota (0-10) o -1 para terminar el bucle: "))
if notas == -1:
    print("fin del bucle.")
    if diezEncontrado:
        print("Se ha encontrado un 10.")
    else:
        print("No se ha encontrado ningún 10.")
