num = int(input("Ingrese un número: "))
if 1<num<101:
    if num % 2 == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")
else:
    print("Número ingresado no válido")