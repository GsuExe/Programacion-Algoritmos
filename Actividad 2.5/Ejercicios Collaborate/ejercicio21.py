#Yo lo trabajaré como un menú para que sea algo más entretenido

opcion = 0
total = 0

print("\tMENÚ")
print("1) Churrasco ---> $1.500")
print("2) Completo ---> $1.000")
print("3) Vegetariano ---> $2.000")
print("4) Barros Luco ---> $3.000")

while opcion != 1:
    while True:
        try:
            sandwich = int(input("\nSeleccione un sándwich: "))
            if 1 <= sandwich <= 4:
                break
            else:
                print("Opción ingresada fuera del rango. Intente nuevamente...")
                print("-" * 55)
        
        except:
            print("Opción ingresada debe ser númerica. Intente nuevamente...")
            print("-" * 55)

    while True:
        try:
            cant = int(input("\nIngrese cantidad que desea llevar: "))
            if cant > 0:
                print("¡¡¡Se agregó a la orden correctamente!!!")
                break
            else:
                print("Cantidad ingresada debe ser por lo menos 1. Intente nuevamente...")
                print("-" * 55)
        except:
            print("Cantidad ingresada debe ser númerica. Intente nuevamente...")
            print("-" * 55)

    if sandwich == 1:
        total += cant * 1500
    elif sandwich == 2:
        total += cant * 1000
    elif sandwich == 3:
        total += cant * 2000
    else:
        total += cant * 3000

    print(f"\nTotal a pagar hasta el momento: ${total}")

    print("\n¿Desea finalizar su orden?")
    print("1) Si")
    print("2) No")

    while True:
        try:
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1 or opcion == 2:
                break
            else:
                print("Opción ingresada fuera de rango. Intente nuevamente...")
                print("-" * 55)
        except:
            print("Opción ingresada debe ser númerica. Intente nuevamente...")
            print("-" * 55)

print("\n¿Tiene un código de descuento?")
print("1) Si")
print("2) No")

        
while True:
    try:
        descuento = int(input("\nIngrese una opción: "))
        if descuento == 1 or descuento == 2:
            break
        else:
            print("Opción ingresada fuera del rango. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Opción ingresada debe ser númerica. Intente nuevamente...")
        print("-" * 55)   

if opcion == 1:
    total -= total * 0.1

print("\nFinalizando orden...")

print(f"Total a pagar: ${int(total)}")
print("-" * 55)