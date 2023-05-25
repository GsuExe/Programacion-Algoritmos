cont_cero = 0
cont_par = 0
suma_par = 0
i = 1

while i <= 5:
    num = int(input("\nIngrese un número entero: "))

    if num > 0:
        cont_cero += 1
    
    if num % 2 == 0:
        cont_par += 1
        suma_par += num

    i += 1

print(f"\nHay {cont_cero} números ingresados que son mayores a cero \nHay {cont_par} números ingresados que son pares y su suma es {suma_par}")