num = int(input("Ingrese un número entero mayor a cero: "))
suma = 0

if num > 0:
    for i in range(1,num):
        if num % i == 0:
            suma += i
    if num == suma:
        print(f"\nEl número {num} es perfecto")
    else:
        print(f"\nEl número {num} NO es perfecto")
else:
    print("\nNúmero ingresado es igual o menor a cero")