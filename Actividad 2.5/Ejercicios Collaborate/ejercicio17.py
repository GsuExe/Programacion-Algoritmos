print("\t \t \tMENÚ")
print("-" * 55)
print("| Plato                               | Tipo          |")
print("-" * 55)
print("| Charquicán con Huevo Frito          | Vegetariano   |")
print("-" * 55)
print("| Salteado de Verduras con Fideos     | Vegano        |")
print("-" * 55)
print("| Lomo a lo pobre                     | Hipercalórico |")
print("-" * 55)

while True:
    try:
        opcion = int(input("\nSeleccione un plato (Considere que están enumerados de 1 a 3): "))
        if 1 <= opcion <= 3:
            break
        else:
            print("Opción ingresada fuera del rango. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Opción ingresada debe ser númerica. Intente nuevamente...")
        print("-" * 55)

while True:
    try:
        cant = int(input("\nIngrese cantidad de platos que desea llevar: "))
        if cant > 0:
            break
        else:
            print("Cantidad ingresada debe ser por lo menos 1. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Cantidad ingresada debe ser númerica. Intente nuevamente...")
        print("-" * 55)

total = cant * 4500
print(f"\nTotal a pagar: ${total}")

while True:
    try:
        efectivo = int(input("\nIngrese efectivo: "))
        if efectivo >= total:
            break
        else:
            print("Cantidad ingresada no es suficiente para pagar el total. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Cantidad ingresada debe ser númerica. Intente nuevamente...")
        print("-" * 55)

print("\nFinalizando orden...")

print("\n \t \t \tBOLETA")

if opcion == 1:
    print("\nCharquicán con Huevo Frito - Vegetariano")
elif opcion == 2:
    print("\nSalteado de Verduras con Fideos - Vegano")
else:
    print("\nLomo a lo Pobre - Hipercalórico")

print(f"Cantidad de Platos: {cant}")
print("-" * 55)

total = cant * 4500

print(f"Total a pagar: ${total}")
print("-" * 55)

print(f"Dinero Ingresado: ${efectivo}")
print(f"Vuelto: ${efectivo - total}")
print("-" * 55)




































