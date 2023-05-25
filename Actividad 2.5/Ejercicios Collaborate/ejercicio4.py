opcion = 0

while opcion != 2:
    while True:
        try:
            num_horas = int(input("\nIngrese número de horas trabajadas: "))
            if num_horas > 0:
                break
            else:
                print("Como mínimo, debe tener 1 hora trabajada. Intente nuevamente...")
                print(45*"-")
        except:
            print("Dato ingresado NO es númerico. Intente nuevamente...")
            print(45*"-")
    
    while True:
        try:
            costo_hora = int(input("\nIngrese el costo por hora trabajada: "))
            if costo_hora >= 1000:
                break
            else:
                print("Como mínimo, el costo por hora trabajada debe ser de $1000")
                print(45*"-")
        except:
            print("Dato ingresado NO es númerico. Intente nuevamente...")
            print(45*"-")
    print("\n")
    print(45*"*")
    print(f"El pago que le corresponde por {num_horas} horas trabajadas es de: ${num_horas * costo_hora}")
    print(45*"*")
    
    print("\n¿Desea continuar haciendo cálculos?")
    print("1) Si")
    print("2) No")

    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if 0 < opcion < 3:
                break
            else:
                print("Opción ingresada fuera de rango. Intente nuevamente...")
                print(45*"-")
        except:
            print("Opción ingresada debe ser númerica. Intente nuevamente...")
            print(45*"-")

print("\nFinalizando proceso...")
print(45*"-")