userName = str(input("Introduce tu nombre: "))
password = str(input("Introduce tu contraseña: "))
if userName == "admin" and password == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")