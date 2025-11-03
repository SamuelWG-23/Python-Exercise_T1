print("Introduce dos números para ordenarlos ")
print("Introduce el primer número")
num1 = float(input())
print("Introduce el segundo número")
num2 = float(input())
if num1>num2:
    print(f"El orden de los números introducidos es {num1} > {num2}")
elif num2>num1:
    print(f"El orden de los números introducidos es {num2} > {num1}")
else:
    print("Los números son iguales")