print("Introduce tres números para ordenarlos ")
print("Introduce el primer número")
num1 = float(input())
print("Introduce el segundo número")
num2 = float(input())
print("Introduce el tercer número")
num3 = float(input())
if num1==num2==num3:
    print("Los números son iguales")
while num1<num2 or num2<num3:
    if num1<num2:
        num1 = num1+num2
        num2 = num1-num2
        num1 = num1-num2
    if num2<num3:
        num2 = num2+num3
        num3 = num2-num3
        num2 = num2-num3
print(f"Los números ordenados son {num1}, {num2}, {num3}")
