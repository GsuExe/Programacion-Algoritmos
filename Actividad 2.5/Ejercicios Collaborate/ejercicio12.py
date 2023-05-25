while True:
    print("\nInversionista N°1")
    try:
        inv1 = int(input("Ingrese inversión: "))
        if inv1 > 0:
            break
        else:
            print("Inversión ingresada debe ser mayor a cero. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Opción ingresada debe ser de tipo Entero. Intente nuevamente...")
        print("-" * 55)

while True:
    print("\nInversionista N°2")
    try:
        inv2 = int(input("Ingrese inversión: "))
        if inv2 > 0:
            break
        else:
            print("Inversión ingresada debe ser mayor a cero. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Opción ingresada debe ser de tipo Entero. Intente nuevamente...")
        print("-" * 55)

while True:
    print("\nInversionista N°3")
    try:
        inv3 = int(input("Ingrese inversión: "))
        if inv3 > 0:
            break
        else:
            print("Inversión ingresada debe ser mayor a cero. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Opción ingresada debe ser de tipo Entero. Intente nuevamente...")
        print("-" * 55)

print("\nRealizando cálculos...")

total = inv1 + inv2 + inv3

pct1 = round((inv1 * 100) / total,2)
pct2 = round((inv2 * 100) / total,2)
pct3 = round((inv3 * 100) / total,2)


print(f"\nTotal de la inversión: ${total}")
print(f"Porcentaje que aporta el primer inversionista: %{pct1}")
print(f"Porcentaje que aporta el segundo inversionista: %{pct2}")
print(f"Porcentaje que aporta el tercer inversionista: %{pct3}")
print("-" * 55)

