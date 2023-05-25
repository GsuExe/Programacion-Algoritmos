from random import randint

for i in range(1,16):
    num = randint(100,500)
    print (f"N°{i}: ")
    print(f"El número obtenido es {num}")
    if num % 2 == 0:
        print("El número es par")
        print("-" * 35)
    else:
        print("El número es impar")
        print("-" * 35)