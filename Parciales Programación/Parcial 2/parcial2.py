opcion = 0

total = 0

trat1 = 250000
trat2 = 475000
trat3 = 800000

cant_trat1 = 0
cant_trat2 = 0
cant_trat3 = 0

descuento = 0

while opcion != 3:
    print("\n")
    print("*" * 55)
    print("MENÚ 'El Diente de Oro'")
    print("1) Cotización")
    print("2) Renunciar")
    print("3) Salir")
    print("*" * 55)
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if 1 <= opcion <= 3:
                break
            else:
                print("Opción ingresada fuera del rango. Intente nuevamente...")
                print("-" * 55)
        except:
            print("Opción ingresada debe ser númerica. Intente nuevamente...")
            print("-" * 55)
    
    if opcion == 1:
        continuar = 0
        print("\n")
        print("*" * 55)
        print("Tratamientos Disponibles")
        print("1) Carillas Porcelana ---> $250.000")
        print("2) Implantes Dentales ---> $475.000")
        print("3) Ortodoncia Brackets ---> $800.000")
        print("*" * 55)
        while continuar != 2: 
            while True:
                try:
                    tratamiento = int(input("\nSeleccione un tratamiento: "))
                    if 1 <= tratamiento <= 3:
                        break
                    else:
                        print("Opción ingresada fuera de rango. Intente nuevamente...")
                        print("-" * 55)
                except:
                    print("Opción ingresada debe ser númerica. Intente nuevamente...")
                    print("-" * 55)
            while True:
                try:
                    cantidad = int(input("\nIngrese cantidad que desea del tratamiento seleccionado: "))
                    if cantidad > 0:
                        print("¡¡¡Tratamiento(s) agregados correctamente!!!")
                        break
                    else:
                        print("Cantidad ingresada debe ser por lo menos 1. Intente nuevamente...")
                        print("-" * 55)
                except:
                    print("Cantidad ingresada debe ser númerica. Intente nuevamente...")
                    print("-" * 55)

            if tratamiento == 1:
                total += trat1 * cantidad
                cant_trat1 += cantidad
            elif tratamiento == 2:
                total += trat2 * cantidad
                cant_trat2 += cantidad
            else:
                total += trat3 * cantidad
                cant_trat3 += cantidad

            while True:
                print("\n¿Desea agregar otro tratamiento?")
                print("1) Si")
                print("2) No")
                try:
                    continuar = int(input("\nSeleccione una opción: "))
                    if continuar == 1 or continuar == 2:
                        break
                    else:
                        print("Opción ingresada fuera del rango. Intente nuevamente...")
                        print("-" * 55)
                except:
                    print("Opción ingresada debe ser númerica. Intente nuevamente...")
                    print("-" * 55)
            
            
        while True:
            print("\n")
            print("*" * 55)
            print("Descuentos de Trabajadores")
            print("1) Trabajador Auxiliar ---> 15%")
            print("2) Trabajador Administrativo ---> 10%")
            print("3) Trabajador Docente ---> 5%")
            print("*" * 55)
            try:
                trabajador = int(input("\nSeleccione su tipo de Trabajador: "))
                if 1 <= trabajador <= 3:
                    print("¡¡¡Descuento aplicado correctamente!!!")
                    break
                else:
                    print("Opción ingresada fuera del rango. Intente nuevamente...")
                    print("-" * 55)
            except:
                print("Opción ingresada debe ser númerica. Intente nuevamente...")
                print("-" * 55)

        total_sin_descuento = total

        if trabajador == 1:
            descuento = 0.15
            total -= total * descuento
        elif trabajador == 2:
            descuento = 0.10
            total -= total * descuento
        else:
            descuento = 0.05
            total -= total * descuento

        cuota = total / 12
        
        #BOLETA
        print("\n")
        print("-" * 55)
        print("\tCotización:")
        print("-" * 55)
        if cant_trat1 > 0:
            print(f"--> {cant_trat1} tratamiento(s) Carillas Porcelana ${trat1 * cant_trat1}")
        if cant_trat2 > 0:
            print(f"--> {cant_trat2} tratamiento(s) Implantes Dentales ${trat2 * cant_trat2}")
        if cant_trat3 > 0:
            print(f"--> {cant_trat3} tratamiento(s) Ortodoncia Brackets ${trat3 * cant_trat3}")
        print("-" * 55)
        print(f"Subtotal \t${int(total_sin_descuento)}")
        print(f"Descuento {int(descuento * 100)}% \t${round(total_sin_descuento * descuento)}")
        print("-" * 55)
        print(f"Total \t${round(total)}")
        print("-" * 55)
        print(f"Son 12 cuotas de: ${round(cuota)}")
        print("\nSonría Bonito!!!")

    elif opcion == 2:
        total = 0
        cant_trat1 = 0
        cant_trat2 = 0
        cant_trat3 = 0
        print("\nEliminando cotización previa...")
        print("¡¡¡Ya puede comenzar una nueva cotización!!!")
    
    else:
        print("\nSaliendo del programa...")
        print("-" * 55)