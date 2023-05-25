while True:
    try:
        n=int(input())
        r=587/n
        print(n)
        break
    except ZeroDivisionError:
        print("No puede dividir por CERO!!!")
    except ValueError:
        print("Debe ingresar un n°!!!")
    except:
        print("Error")
