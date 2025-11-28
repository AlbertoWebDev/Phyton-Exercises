try:
	num = int(input("Introduce un número de dos cifras:"))
except ValueError:
	print("Introduce un número.")
else:
	if not (10 <= num <= 99):
		print("El número no tiene dos cifras, introduce otro.")
	else:
		num_invertido = (num % 10) * 10 + (num // 10)
		print("El número invertido es: " , num_invertido)