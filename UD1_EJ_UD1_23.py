print("Introduce números para saber si has añadido un número negativo y cuantos positivos y negativos")
print("Usa el 0 para calcular:")
num = 1
negativo = 0
positivo = 0
while num!=0:
    print("Introduce un número")
    num = int(input())
    if num>0:
        positivo+=1
    if num<0:
        negativo+=1
if negativo>=1:
    print(f"Has introducido al menos un número negativo. Has introducido {positivo} números positivos y {negativo} números negativos.")
else:
    print(f"No has introducido ningún número negativo. Has introducido {positivo} números positivos")
