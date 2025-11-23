pares = 0
impares = 0
for i in range(101, 200):
    if i % 2 == 0:
        pares += i
    else:
        impares += i
print("La suma de todos los pares es: " + str(pares))
print("La suma de todos los impares es: " + str(impares))
