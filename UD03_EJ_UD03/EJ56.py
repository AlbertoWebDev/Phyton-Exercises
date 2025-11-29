while True:
    try:
        n_primos = int(input("Introduce la cantidad (N) de números primos que deseas mostrar: "))
    except ValueError:
        print("Error, debes introducir un número entero.")
        continue
    
    if n_primos > 0:
        break
    else:
        print("Error, la cantidad debe ser un número entero positivo mayor que cero.")


numeros_encontrados = 0
numero_actual = 2  # Empezamos en el primer primo

print("Los", n_primos, "primeros números primos son:")

while numeros_encontrados < n_primos:
    
    es_primo = True
    
    if numero_actual <= 1:
        es_primo = False
    divisor = 2
    while divisor < numero_actual:
        if numero_actual % divisor == 0:
            es_primo = False
            break
        divisor = divisor + 1

    if es_primo:
        print(numero_actual)
        numeros_encontrados = numeros_encontrados + 1
        
    numero_actual = numero_actual + 1