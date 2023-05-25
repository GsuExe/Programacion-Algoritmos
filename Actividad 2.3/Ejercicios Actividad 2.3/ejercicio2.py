vocales = ["a","e","i","o","u"]
cont_vocales = 0
cont_consonante = 0

for i in range(10):
    letra = input("Ingrese una letra: ")
    if letra in vocales:
        cont_vocales += 1
    else:
        cont_consonante += 1

print(f"Cantidad de vocales ingresadas: {cont_vocales}")
print(f"Cantidad de consonantes ingresadas: {cont_consonante}")

