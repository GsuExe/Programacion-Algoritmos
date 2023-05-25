lado_a = float(input("Ingrese la medida del lado a: "))
lado_b = float(input("Ingrese la medida del lado b: "))
lado_c = float(input("Ingrese la medida del lado c: "))

if lado_a < (lado_b + lado_c) and lado_b < (lado_a + lado_c) and lado_c < (lado_a + lado_b):
    if lado_a == lado_b:
        if lado_b == lado_c:
            print("Tipo de triángulo: equilátero")
        else:
            print("Tipo de triángulo: isósceles")
    elif lado_b == lado_c:
        if lado_c == lado_a:
            print("Tipo de triángulo: equilátero")
        else:
            print("Tipo de triángulo: isósceles")
    elif lado_a == lado_c:
        if lado_b == lado_c:
            print("Tipo de triángulo: equilátero")
        else:
            print("Tipo de triángulo: isósceles")
    else:
        print("Tipo de triángulo: escaleno")
else:
    print("Los lados ingresados NO pueden formar un triángulo")


    



