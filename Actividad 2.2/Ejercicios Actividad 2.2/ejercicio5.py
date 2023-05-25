num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

suma = 0
contador = 0

if 0 < num1:
    if num1 % 2 == 0:
        suma += num1
    else:
        contador += 1 
else:
    contador += 1

if 0 < num2:
    if num2 % 2 == 0:
        suma += num2
    else:
        contador += 1 
else:
    contador += 1

if 0 < num3:
    if num3 % 2 == 0:
        suma += num3
    else:
        contador += 1 
else:
    contador += 1

print(f"La suma de los números ingresados que son positivos y pares es de {suma}")
print(f"La cantidad de números negativos o impares es de {contador}")


