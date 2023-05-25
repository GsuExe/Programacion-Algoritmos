cant_zapatos = int(input("Ingrese cantidad de zapatos a comprar: "))

total = cant_zapatos * 20_000

if total >= 40_000:
    print(f"Total de la compra: ${total}")
    print("¡Su envío es gratis!")
else:
    total += 3000
    print(f"Total de la compra: ${total}")