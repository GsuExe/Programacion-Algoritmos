num = int(input("Ingrese un número entero mayor a cero: "))

while num <= 0:
    num = int(input("\nNúmero inválido. Ingrese un número entero mayor a cero: "))

es_primo = True
i = 2 

while i < num:
    if num % i == 0:
        es_primo = False
    i += 1

if es_primo:
    print(f"\nEl número {num} es primo")
else:
    print(f"\nEl número {num} NO es primo")
