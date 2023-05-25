#Calcular el factorial 

num = int(input("Ingrese un número: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"El factorial del número {num} es {factorial}")