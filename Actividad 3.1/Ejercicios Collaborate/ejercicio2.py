nombres = []

opcion = 0

cont = 1

while opcion != 2:
    print(f"\nNombre N°{cont}")
    while True:
        try:
            nom = input("Ingrese un nombre: ")
            if not nom.isalpha():
                raise Exception()
            else:
                if nom not in nombres:
                    print(f"¡¡¡El nombre {nom} ha sido ingresado correctamente!!!")
                    nombres.append(nom)
                    cont += 1
                    break
                else:
                    print(f"Ese nombre ya ha sido ingresado en la lista. Intente nuevamente...")
                    print("-" * 55)
        except:
            print("Nombre ingresado debe ser de tipo String. Intente nuevamente...")
            print("-" * 55)
     
   
    print("\n¿Desea seguir ingresando nombres?")
    print("[1] Si")
    print("[2] No")

    while True:

        try:
             opcion = int(input("Seleccione una opción: "))
             if opcion == 1 or opcion == 2:
                  break
             else:
                  print("Opción ingresada fuera del rango. Intente nuevamente...")
                  print("-" * 55)
        except:
             print("Opción ingresada debe ser númerica. Intente nuevamente...")
             print("-" * 55)

    if opcion == 1:
         print("Continuando proceso...")
    else:
        print("Finalizando proceso...")
        break
    
    print("-" * 40)

print(f"\nLista de nombres \n{nombres}")

menor = 999

for i in range(len(nombres)):
     if len(nombres[i]) < menor:
          menor = len(nombres[i])
          pos = i

print(f"\nEl nombre más corto es {nombres[pos]} y tiene {menor} caracteres.")
print(f"{nombres[pos]} procederá a ser eliminad@ de la existencia.")

nombres.pop(pos)

print(f"\nNueva lista de nombres \n{nombres}")
print("-" * 55)