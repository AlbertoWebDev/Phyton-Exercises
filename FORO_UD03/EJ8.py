try:
    n = int(input("Introduce el valor de n: "))
    
except ValueError:
    print("Por favor, introduce un número entero válido.")
    exit()
    
if n > 0:
    # Parte superior
	for i in range(1, n + 1):
		spaces = n - i
		stars = 2 * i - 1
		print(' ' * spaces + '*' * stars)

	# Parte inferior
	for i in range(n - 1, 0, -1):
		spaces = n - i
		stars = 2 * i - 1
		print(' ' * spaces + '*' * stars)
else:
	print("n debe ser mayor o igual que 1")

