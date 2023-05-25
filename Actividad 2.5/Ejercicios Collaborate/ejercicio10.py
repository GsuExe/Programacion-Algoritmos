while True:
    try:
        num1 = int(input("\nIngrese primer número entero: "))
        if isinstance(num1,int):
            break
    except:
        print("Dato ingresado NO es entero. Intente nuevamente...")
        print(35*"-")

while True:
    try:
        num2 = int(input("\nIngrese segundo número entero: "))
        if isinstance(num2,int):
            break
    except:
        print("Dato ingresado NO es entero. Intente nuevamente...")
        print(35*"-")

print("\n")
if num1 % num2 == 0:
    print(f"{num1} es divisible por {num2} ")
else:
    print(f"{num1} NO es divisible por {num2} ")

if num2 % num1 == 0:
    print(f"{num2} es divisible por {num1}")
else:
    print(f"{num2} NO es divisible por {num1}")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Ambos números son iguales")

if num1 % 2 != 0 and num2 % 2 != 0:
    print("Ambos números son impares")
else:
    print("Alguno de los números ingresados NO es impar")

print(45*"-")

    