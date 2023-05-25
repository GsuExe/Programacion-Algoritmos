# Angel Gonzalez
"""Menú IVA"""
opcion = 0
while opcion != 2:
    print(35*"*")
    print("""(1) Para calcular IVA y precio final\n(2) Para SALIR """)
    print(35*"*")
    while True:
        try:
            opcion = int(input("Ingrese opción : "))
            if 1 <= opcion <= 2:
                break
            else:
                print("Opción ingresada no valida")
                print(35*"-")
        except:
            print("Ingresó valor no valido")
            print(35*"-")
    if opcion == 1:
        try:
            ValorBruto = int(input("Ingrese precio : "))
            if ValorBruto < 1:
                print(35*"-")
                print("El precio ingresado es demasiado bajo")
            else:
                iva = ValorBruto*0.19
                ValorFinal = ValorBruto + iva
                print(f"El valor del IVA es : ${iva}")
                print(f"El valor final es : ${ValorFinal}")
        except:
            print(35*"-")
            print("El valor ingresado no es valido") 
print("Proceso Finalizado")
print(35*"*")