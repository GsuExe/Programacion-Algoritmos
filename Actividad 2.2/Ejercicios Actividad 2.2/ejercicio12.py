#CineDuoc
flag = False
total_entradas = 0
total = 0 

print("*********************** \nBIENVENIDO A CINEDUOC \n***********************")

print("\n¿Pertenece a Duoc? Seleccione una opción:")
print("1) Estudiante")
print("2) Funcionario")
print("3) No pertenece")
opcion = int(input())

if opcion == 1 or opcion == 2:
    flag = True

print("\nSeleccione tipo de entrada:")
print("1) Estreno ---> $4.800")
print("2) Normal ---> $2.900")
opcion = int(input())

cantidad = int(input("\nIngrese la cantidad de entradas que desea comprar: "))

if opcion == 1:
    total_entradas += 4800 * cantidad
else:
    total_entradas += 2900 * cantidad

print("\n¿Desea agregar palomitas de maíz a su pedido?:")
print("1) Si")
print("2) No")
opcion = int(input())

if opcion == 1:
    print("\nSeleccione una opción:")
    print("1) Palomitas Pequeña ---> $2.500")
    print("2) Palomitas Mediana ---> $4.500")
    print("3) Palomitas Grande ---> $7.800")
    opcion = int(input())

    cantidad = int(input("\nIngrese la cantidad de Palomitas que desea comprar: "))

    if opcion == 1:
        total += 2500 * cantidad
    elif opcion == 2:
        total += 4500 * cantidad
    else:
        total += 7800 * cantidad

print("\n¿Desea agregar bebidas a su pedido?:")
print("1) Si")
print("2) No")
opcion = int(input())

if opcion == 1:
    print("\nSeleccione una opción:")
    print("1) Bebida Pequeña ---> $1.000")
    print("2) Bebida Mediana ---> $1.250")
    print("3) Bebida Grande ---> $2.000")
    opcion = int(input())

    cantidad = int(input("\nIngrese la cantidad de Bebidas que desea comprar: "))

    if opcion == 1:
        total += 1000 * cantidad
    elif opcion == 2:
        total += 1250 * cantidad
    else:
        total += 2000 * cantidad

if flag:
    total_entradas -= total_entradas * 0.30
    total += total_entradas
else:
    total += total_entradas

print(f"\nTotal a pagar: ${int(total)}")
efectivo = int(input("Ingrese efectivo: "))
vuelto = efectivo - total
print(f"Su vuelto es de: ${int(vuelto)}")
print("¡¡¡GRACIAS POR SU COMPRA, VUELVA PRONTO!!!")

