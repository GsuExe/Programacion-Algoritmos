"""
while True:
    try:
        peso = int(input("\nIngrese su peso (en kg): "))
        if peso > 0:
            break
        else:
            print("Peso ingresado debe ser mayor a cero. Intente nuevamente...")
            print(35*"-")
    except:
        print("Dato ingresado NO es númerico. Intente nuevamente...")
        print(35*"-")

while True:
    try:
        estatura = float(input("\nIngrese su estatura (en metros): "))
        if estatura > 0:
            break
        else:
            print("Estatura ingresada debe ser mayor a cero. Intente nuevamente...")
            print(35*"-")

    except:
        print("Dato ingresado NO es númerico. Intente nuevamente...")
        print(35*"-")

imc = round(peso / (estatura ** 2),2)
print(35*"*")
print(f"Tu índice de masa corporal es: {imc}")
print(35*"*")
"""
while True:
        try:
            height = float(input("Ingrese la altura:\n"))
            verHeight = float(height).is_integer()
            if verHeight == False:
                break
            elif verHeight == 1.0 or verHeight == 1.00 or 1:
                break
            else:
                print("por favor ingrese en numeros decimales")
        except:
            print("ingreso valores no validos por favor ingresa tu altura en (entero).(decimales)")