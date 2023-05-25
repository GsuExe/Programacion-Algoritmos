print("******************** \nTablas números pares \n********************")

for i in range(1,11):
    if i % 2 == 0:
        print(f"\nTabla del {i}")
        for x in range(1,11):
            print(f"{i} * {x} = {i * x}")