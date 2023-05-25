cont_mayor = 0
cont_menor = 0
cont_cero = 0

for i in range(5):
    num = int(input("Ingrese un número entero: "))
    if num > 0:
        cont_mayor += 1
    elif num < 0:
        cont_menor += 1
    else:
        cont_cero += 1

print(f"\nCantidad de números mayores a cero: {cont_mayor}")
print(f"Cantidad de números menores a cero: {cont_menor}")
print(f"Cantidad de números iguales a cero: {cont_cero}")