num1 = int(input("Ingrese el primer número: "))

if num1 > 0:
    num2 = int(input("Ingrese el segundo número: "))
    if num2 > 0:
        suma = num1 + num2
        print(f"La suma de los números {num1} y {num2} es {suma}")
    else:
        print("El segundo número ingresado NO es un entero positivo")
         
else:
    print("El primer número ingresado NO es un entero positivo")