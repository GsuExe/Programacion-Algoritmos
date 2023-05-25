#Asumí que todos los pagos realizados serán del mismo tipo, ya sea Efectivo u Online. 
#Asumí que, en el caso de pago Efectivo, todos los pagos serán realizados en el mismo lugar. Por ende, solo hay 1 recargo. 

opcion = 0

cant_cuentas = 0

total = 0

recargo1 = 2500
recargo2 = 4000
recargo3 = 6000

print("Modalidades de Pago")
print("1) Efectivo")
print("2) Online")

while True:
    try:
        modalidad = int(input("\nSeleccione una opción: "))
        if modalidad == 1 or modalidad == 2:
            break
        else:
            print("Opción ingresada fuera del rango. Intente nuevamente...")
            print("-" * 55)

    except:
        print("Opción ingresada debe ser númerica. Intente nuevamente...")
        print("-" * 55)


while opcion != 2:
    while True:
        try:
            cuenta = int(input("\nIngrese monto de cuenta a pagar: "))
            if cuenta > 0:
                print("¡¡¡Cuenta agregada con éxito!!!")
                cant_cuentas += 1
                break
            else:
                print("Cantidad ingresada debe ser mayor a cero. Intente nuevamente...")
                print("-" * 55)
        except:
            print("Cantidad ingresada debe ser númerica. Intente nuevamente...")
            print("-" * 55)

    total += cuenta

    print("\n¿Desea agregar más cuentas?")
    print("1) Si")
    print("2) No")

    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1 or opcion == 2:
                break
            else:
                print("Opción ingresada fuera del rango. Intente nuevamente...")
                print("-" * 55)
        except:
            print("Opción ingresada debe ser númerica. Intente nuevamente...")
            print("-" * 55)

if modalidad == 1:
    while True:
        try:
            lugar_pago = int(input("\nIngrese distancia al lugar del pago (en km): "))
            if lugar_pago > 0:
                break
            else:
                print("Distancia ingresada debe ser por lo menos 1 km. Intente nuevamente...")
                print("-" * 55)
        except:
            print("Distancia ingresada debe ser númerica. Intente nuevamente...")
            print("-" * 55)
    
    if lugar_pago < 10:
        print(f"Su recargo es de: ${recargo1}")
        total += recargo1
    elif 10 <= lugar_pago < 21:
        print(f"Su recargo es de: ${recargo2}")
        total += recargo2
    else:
        print(f"Su recargo es de: ${recargo3}")
        total += recargo3
else:
    total += 600 * cant_cuentas

print("\nFinalizando cálculos...")
print(f"\nTotal a pagar: ${total}")
print("-" * 55)