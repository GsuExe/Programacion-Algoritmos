num = int(input("Ingrese un número entero mayor a cero: "))

while num <= 0:
    num = int(input("\nNúmero inválido. Ingrese un número entero mayor a cero: "))

suma = 0
i = 1 

while i < num:
    if num % i == 0:
        suma += i
    i += 1

if num == suma:
    print(f"\nEl número {num} es perfecto")
else:
    print(f"\nEl número {num} NO es perfecto")
