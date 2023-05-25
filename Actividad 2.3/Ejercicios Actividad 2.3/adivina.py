import random

x = random.randint(1,10)

fallaste = True

for i in range(1,4):
    print(f"\nIntento N°{i}")
    num = int(input("\nIngrese un número: "))
    if num > x:
        print("\n¡¡¡FALLASTE!!!")
        print(f"El número ingresado {num} es mayor al número mágico")
        
    elif num < x:
        print("\n¡¡¡FALLASTE!!!")
        print(f"El número ingresado {num} es menor al número mágico")
    else:
        print("¡¡¡ACERTASTE!!!")
        print(f"El número mágico era {x}")
        fallaste = False
        break

if fallaste:
    print("\n¡¡¡SE ACABARON LOS INTENTOS!!! \n¡¡¡HAS PERDIDO!!! \nEl número mágico era {x}")