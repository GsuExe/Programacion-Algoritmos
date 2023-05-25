while True:
    try:
        distancia = float(input("\nIngrese la distancia a recorrer (en km): "))
        if distancia > 0:
            break
        else:
            print("Distancia ingresada debe ser por lo menos 1 km. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Distancia ingresada debe ser númerica. Intente nuevamente...")
        print("-" * 55)

while True:
    try:
        dias_estancia = int(input("\nIngrese cantidad de días de estancia: "))
        if dias_estancia > 0:
            break
        else:
            print("Días ingresados deben ser por lo menos 1. Intente nuevamente...")
            print("-" * 55)
    except:
        print("Días ingresados deben ser númericos. Intente nuevamente...")
        print("-" * 55)

precio_km = 1200
total = distancia * precio_km

if dias_estancia > 7 and distancia > 800:
    total -= total * 0.3

print("\nFinalizando cálculos...")

print(f"\nEl precio del boleto es de: ${int(total)}")
print("-" * 55)
