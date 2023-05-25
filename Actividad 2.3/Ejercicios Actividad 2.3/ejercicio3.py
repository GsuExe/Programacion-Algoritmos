num = int(input("Ingrese un número entero mayor a cero: "))

primo = True

if num > 0:
    for i in range(2,num):
        if num % i == 0:
            primo = False
            break
else:
    print("\nNúmero ingresado es igual o menor a cero")

if primo:
    print("\nEl número ingresado es primo")
else:
    print("\nEl número ingresado NO es primo")