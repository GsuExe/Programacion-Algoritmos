'''
En un delivery se venden 4 tipos de pan:
Amasado $1.500 
Molde $1.000 
Baguette $2.000 
Integral $3.000 

Determine el total a pagar por un cliente, el cual puede comprar diferentes tipos y cantidad de pan. 
Si el total de la venta es superior a $5000 el envío es gratis, sino se cobra el 10% adicional. 
Muestre los mensajes correspondientes.
'''
subTotal=0
opc=0
while opc!=5:
    print("&"*40)
    print("\tMenú DeliveryPan")
    print("&"*40)
    print("1.- Amasado $1500")
    print("2.- Molde $1000")    
    print("3.- Baguette $2000")
    print("4.- Integral $3000")
    print("5.- Ver Total")
    while True:
        try:
            opc=int(input("Ingrese su opción: "))
            if 0<opc<6:
                break
            else:
                print("Opción fuera de rango!!")
        except:
            print("Opción es un N°!!!")
    if opc==1:
        subTotal+=1500
    elif opc==2:
        subTotal+=1000
    elif opc==3:
        subTotal+=2000
    elif opc==4:
        subTotal+=3000
    else:
        if subTotal>5000:
            envio=0
            print("Envío Gratis")
        else:
            envio=subTotal*0.1
        print(f"Total a pagar: ${subTotal+envio}")
print("Hasta Pronto!!")