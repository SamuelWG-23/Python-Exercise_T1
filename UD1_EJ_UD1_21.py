cantidad = 100
contador = cantidad
negativo = 0
numero = 1
print(f"Introduce {cantidad} números que no sean nulos para saber si has introducido algun numero negativo")
while contador>0:
    numero = int(input(f"Introduce un número. Faltan {contador}. "))
    if numero == 0:
        print("Introduce un numero que no sea 0")
    else:
        if numero<0:
            negativo+=1
            contador-=1
        else:
            contador-=1
if negativo>0:
    print("Has introducido al menos un número negativo")
else:
    print("No has introducido ningun número negativo")
