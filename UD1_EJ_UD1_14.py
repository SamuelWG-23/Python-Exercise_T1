
print("Introduce el primer número")
num1 = int(input())
print("Introduce el segundo número")
num2 = int(input())
if num2 == 0:
    print(f"Siendo los números: {num1} y {num2} la suma es ", num1+num2, "la resta ", num1-num2," la multiplicacion ", num1*num2, " y la división no puede ser realizada al ser el divisor 0")
else:
    print(f"Siendo los números: {num1} y {num2} la suma es ", num1+num2, "la resta ", num1-num2," la multiplicacion ", num1*num2, " y la división ",num1/num2)
    

