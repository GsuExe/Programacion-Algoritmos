churrasco = int(input("¿Cuántos churrascos desea llevar? "))
completo = int(input("¿Cuántos completos desea llevar? "))
vegetariano = int(input("¿Cuántos vegetarianos desea llevar? "))
barros_luco = int(input("¿Cuántos barros luco desea llevar? "))

total = churrasco * 1500 + completo * 1000 + vegetariano * 2000 + barros_luco * 3000

descuento = input("\n¿Tiene un código de descuento? (Responda SI o NO): ")

if descuento == "SI":
    total -= total * 0.10

print(f"Total de compra: ${int(total)}")