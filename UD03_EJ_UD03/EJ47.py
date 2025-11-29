import math

try:
    numero = int(input("Introduce un número entero para comprobar si es primo: "))
except ValueError:
    print("Error, la entrada no es un número entero válido.")
else:
    
    es_primo = True
    
    if numero <= 1:
        es_primo = False
        
    # El número 2 es el único primo par
    elif numero == 2:
        es_primo = True
        
    else:
        limite_superior = math.isqrt(numero)
        
        for divisor in range(2, limite_superior + 1):
            
            if numero % divisor == 0:
                es_primo = False
                break
                
    print("Número introducido:", numero)
    
    if es_primo:
        print("El número", numero, "es un número PRIMO.")
    else:
        print("El número", numero, "NO es un número primo.")