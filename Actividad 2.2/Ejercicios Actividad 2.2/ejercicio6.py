num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

contador = 0

if num1 < 0:
    contador += 1

if num2 < 0:
    contador += 1

if num3 < 0:
    contador += 1

print(f"Cantidad de números menores a cero: {contador}")
