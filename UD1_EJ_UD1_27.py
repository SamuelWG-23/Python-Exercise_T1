print("Introduce notas hasta que añadas un -1 para saber cuantos 10 has introducido")
dieces = 0
num = 0
while num != -1:
    (print(f"Introduce una nota "))
    num = float(input())
    if num == 10:
        dieces+=1
    if num < -1 or num > 10:
        print("Introduce una nota válida")
print(f"Se han introducido {dieces} veces la nota 10")