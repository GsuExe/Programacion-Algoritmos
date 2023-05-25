num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 > num2:
    print(f"El número {num1} es mayor al número {num2}")
elif num2 > num1:
    print(f"El número {num2} es mayor al número {num1}")
else:
    print("Ambos números son iguales")