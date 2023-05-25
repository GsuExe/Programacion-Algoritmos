print("********************* \nTablas de Multiplicar \n*********************")

for factor in range(1,11):
    print(f"\nTabla del {factor}")
    for multiplicacion in range(1,11):
        print(f"{factor} * {multiplicacion} = {factor * multiplicacion}")