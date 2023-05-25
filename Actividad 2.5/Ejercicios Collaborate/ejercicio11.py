opcion = 0

while opcion!=2:
    while True:
        try:
            sexo = input("\nIngrese su sexo (M si es masculino o F si es femenino): ")
            #Este If pregunta si la variable es de tipo entero positiva, negativo o de tipo decimal 
            if sexo.isdigit() or (sexo.startswith('-') and sexo[1:].isdigit()) or sexo.replace('.', '', 1).isdigit(): 
                raise ValueError
            else:
                if sexo.upper() == "M" or sexo.upper() == "F":
                    break
                else:
                    print("String ingresado debe ser 'M' o 'F'. Intente nuevamente...")
                    print("-" * 55)
        except ValueError:
            print("Opción ingresada debe ser un String. Intente nuevamente...")
            print("-" * 55)

    while True:
        try:
            edad = int(input("\nIngrese su edad: "))
            if edad > 0:
                break
            else:
                print("Edad ingresada debe ser mayor a cero. Intentar nuevamente...")
                print("-" * 55)
        except:
            print("Opción ingresada debe ser númerica. Intentar nuevamente...")
            print("-" * 55)

    if sexo.upper() == "M":
        num_pulsaciones = (210 - edad) / 10
    elif sexo.upper() == "F":
        num_pulsaciones = (220 - edad) / 10

    print(f"\nSu número de pulsaciones por cada 10 seg. de ejercicio aeróbico son {num_pulsaciones}")

    while True:
        print("\n¿Desea seguir realizando cálculos?")
        print("1) Si")
        print("2) No")
        try:
            opcion = int(input())
            if 1 <= opcion <= 2:
                break
            else:
                print("Opción ingresada fuera de rango. Intentar nuevamente...")
                print("-" * 55)
        except:
            print("Opción ingresada debe ser númerica. Intentar nuevamente...")
            print("-" * 55)
    
    if opcion == 1:
        print("\nReiniciando...")
        print("-" * 55)
    elif opcion == 2:
        print("\nFinalizando...")
        print("-" * 55)
