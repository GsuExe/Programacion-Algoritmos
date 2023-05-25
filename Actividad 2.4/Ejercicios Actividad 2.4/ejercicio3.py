suma = 0
i = 1


while i <= 5:
    while True:
        print(f"\nIngrese N°{i}: ")
        num = int(input())

        if num > 0:
            suma += num
            break
        else:
            print("Número no válido. Ingrese nuevamente...")
    i += 1

print(f"La suma de los números ingresados es {suma}")