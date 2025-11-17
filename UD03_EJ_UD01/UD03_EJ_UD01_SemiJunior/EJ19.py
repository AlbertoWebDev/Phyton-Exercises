initialMoney = 1000

print("Bienvenido a su cajero virtual! \n")
print("1. Ingresar Dinero en la cuenta \n2. Retirar Dinero de la cuenta \n3. Salir \n")
option = int(input("Seleccione una opción: "))
if option == 1:
    deposit = float(input("Cuanto dinero quieres ingresar?"))
    initialMoney += deposit
    print("has inbgresado ", deposit, " tu saldo actual es de ", initialMoney)
elif option == 2:
    withdraw = float(input("Cuanto dinero quieres retirar?"))
    if withdraw > initialMoney:
        print("No tienes suficiente saldo para retirar esa cantidad")
    else:
        initialMoney -= withdraw
        print("has retirado ", withdraw, " tu saldo actual es de ", initialMoney)
elif option == 3:
    print("Gracias por usar el cajero virtual. ¡Hasta luego!")
else:
    print("Opción no válida. Por favor, seleccione una opción correcta.")