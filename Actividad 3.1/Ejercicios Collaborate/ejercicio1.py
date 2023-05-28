nombres = []
apellidos = []

for i in range(1,4):
    print(f"\nPersona N°{i}")
    while True:
        try:
            nom = input("Ingrese su nombre: ")
            if not nom.isalpha():
                raise Exception()
            else:
                nombres.append(nom)
                break
        except:
            print("Nombre ingresado debe ser de tipo String. Intente nuevamente...")
            print("-" * 55)

    while True:
        try:
            ap = input("Ingrese su apellido: ")
            if not ap.isalpha():
                raise Exception()
            else:
                apellidos.append(ap)
                break
        except:
            print("Nombre ingresado debe ser de tipo String. Intente nuevamente...")
            print("-" * 55)
            

print("\nNombres Ordenados:")
for i in range(len(nombres)):
    print(nombres[i],apellidos[i])