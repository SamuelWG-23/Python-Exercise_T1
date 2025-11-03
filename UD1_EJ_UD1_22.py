cantidad = 100
contador = cantidad
negativo = 0
positivo = 0
numero = 1
print(f"Introduce {cantidad} números que no sean nulos para saber si has introducido algun numero negativo")
while contador>0:
    numero = int(input(f"Introduce un número. Faltan {contador}. "))
    if numero == 0:
        print("Introduce un numero que sea distinto a 0")
    else:
        if numero<0:
            negativo+=1
            contador-=1
        else:
            positivo+=1
            contador-=1

print(f"Has introducido {positivo} números positivos y {negativo} números negativos")

