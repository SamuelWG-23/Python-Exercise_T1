sumaPar = 0
sumaImpar = 0

for i in range (100,201):
    if i%2 == 0:
        sumaPar+=i
    else:
        sumaImpar+=i
print(f"Valor de suma de impares = {sumaImpar}")
print(f"Valor de suma de pares = {sumaPar}")