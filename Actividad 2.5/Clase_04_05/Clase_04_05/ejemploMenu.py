opc=0
while opc!=3:    
    print("&"*30)
    print("\tMenú")
    print("&"*30)
    print("1.- Par o Impar")
    print("2.- Fibonacci")
    print("3.- SALIR")
    while True:
        try:
            opc=int(input("Ingrese su opción: "))
            if 1<=opc<=3:
                break
            else:
                print("Opción Fuera de Rango")
        except:
            print("Opción es un Número!!!")
    if opc==1:
        while True:
            try:
                num=int(input("Ingrese un n°: "))
                break
            except:
                print("Debe ingresar un NÚMERO!!")
        if num%2==0:
            print("PAR")
        else:
            print("IMPAR")
    elif opc==2: #muestre la serie Fibonacci de los primeros 10 números
        n1=1
        n2=2
        cont=0
        while cont<20:
            print(n1)
            ant=n1+n2
            n1=n2
            n2=ant
            cont+=1
print("ADIOS")
    