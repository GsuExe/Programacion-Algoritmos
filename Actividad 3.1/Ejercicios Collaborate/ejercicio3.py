opcion = 0

total = 0

canasta = []

productos = ["Carne molida vacuno", "Pechuga entera de pollo", "Aceite Vegetal", "Bebida Pepsi", "Papel Higiénico Confort"]
contadores = [0, 0, 0, 0, 0]
precios = [3000, 3500, 1700, 1900, 1200]

while True:
    print("\nMenú Principal")
    print("[1] Agregar productos")
    print("[2] Ver canasta")
    print("[3] Total compra")

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
        opcion2 = 0

        print("\n \t \t PRODUCTOS")
        print("-" * 39)
        print("| Producto                  | Precio  |")
        print("-" * 39)
        print(f"| Carne molida vacuno       | $3000   |")
        print("-" * 39)
        print(f"| Pechuga entera de pollo   | $3500   |")
        print("-" * 39)
        print(f"| Aceite vegetal            | $1700   |")
        print("-" * 39)
        print(f"| Bebida Pepsi              | $1900   |")
        print("-" * 39)
        print(f"| Papel Higiénico Confort   | $1200   |")
        print("-" * 39)
        
        #Generación menú productos automático 
        '''
        for i in range(len(productos)):
            print(f"[{len(productos) - (len(productos) - (i + 1))}] {productos[i]} ---> ${precios[i]}")
        '''

        while True:

            while True:
                try:
                    opcion2 = int(input("\nSeleccione un producto (Considere que están enumerados de 1 a 5): "))
                    if 1 <= opcion2 <= 5:
                        opcion2 -= 1

                        if productos[opcion2] not in canasta:
                            canasta.append(productos[opcion2])
                        print(f"¡¡¡Ha seleccionado {productos[opcion2]}!!!")

                        break
                    else:
                        print("Opción ingresada fuera del rango. Intente nuevamente...")
                        print("-" * 55)
                except:
                    print("Opción ingresada debe ser númerica. Intente nuevamente...")
                    print("-" * 55)
        
            while True:
                try:
                    cantidad = int(input(f"\nIngrese cantidad de {productos[opcion2]} que desea llevar: "))
                    if 0 < cantidad:
                        print(f"¡¡¡{cantidad} unidad(es) de {productos[opcion2]} han sido agregado(s) correctamente a la canasta!!!")
                        contadores[opcion2] += cantidad
                        break
                    else:
                        print("Cantidad ingresada debe ser al menos 1. Intente nuevamente...")
                        print("-" * 55)
                except:
                    print("Cantidad ingresada debe ser númerica. Intente nuevamente...")
                    print("-" * 55)


            print("\n¿Desea seguir agregando productos a la canasta?")
            print("[1] Si")
            print("[2] No")

            while True:
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

            if continuar == 1:
                print("Continuando proceso...")
                print("-" * 55)
            else:
                print("Regresando al menú principal...")
                print("-" * 55)
                break
    
    elif opcion == 2:
        if len(canasta) == 0:
            print("¡¡¡Aún no ingresa ningún producto a la canasta!!!")
            print("Regresando al menú principal...")
            print("-" * 55)
        else:
            print("\n \t CANASTA")

            for i in range(len(canasta)):
                for x in range(len(productos)):
                    if canasta[i] == productos[x]:
                        print(f"{productos[x]}  x  {contadores[x]}")

            print("\nRegresando al menú principal...")
            print("-" * 55)
    
    else:
        if len(canasta) == 0:
            print("¡¡¡Aún no ingresa ningún producto a la canasta!!!")
            print("Regresando al menú principal...")
            print("-" * 55)
        else:
            print("\n \t BOLETA:")
            print("-" * 55)

            for i in range(len(canasta)):
                for x in range(len(productos)):
                    if canasta[i] == productos[x]:
                        print(f"---> {contadores[x]} unidades {productos[x]} ${contadores[x] * precios[x]}")
                        total += contadores[x] * precios[x]
            
            print("-" * 55)
            print(f"Total de la compra: ${total}")

            print("\n¿Desea finalizar su compra?")
            print("[1] Si")
            print("[2] No")

            while True:
                try:
                    finalizar = int(input("\nSeleccione una opción: "))
                    if finalizar == 1 or finalizar == 2:
                        break
                    else:
                        print("Opción ingresada fuera del rango. Intente nuevamente...")
                        print("-" * 55)
                except:
                    print("Opción ingresada debe ser númerica. Intente nuevamente...")
                    print("-" * 55)

            if finalizar == 1:
                print("Finalizando compra...")
                print("-" * 55)
                break
            else:
                total = 0
                print("Regresando al menú principal...")
                print("-" * 55)
    

        



            