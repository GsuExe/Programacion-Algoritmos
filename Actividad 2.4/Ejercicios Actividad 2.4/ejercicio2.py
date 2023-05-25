num = int(input("Ingrese un número: "))
factorial = 1

while num > 1:
    factorial *= num
    num -= 1

print(f"El factorial del número es {factorial}")