while True:
    num = int(input("\nIngrese un número entero positivo entre 103 y 987: "))

    if 103 <= num <= 987:
        num_invertido = 0
        while num > 0:
            resto = num - ((num // 10) * 10)
            num_invertido = num_invertido * 10 + resto
            num //= 10
        break
    else:
        print("Número inválido. Ingrese nuevamente...")
    
print(f"\nEl número invertido es: {num_invertido}")