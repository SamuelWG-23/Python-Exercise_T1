num = int(input("Calcula el factorial de un número "))
factorial = 1
contador = num
if num == 0:
    print(factorial)
elif num > 0:
    while num>0:
        factorial*=num
        num-=1
        
    print(factorial)
else:
    print("Numero no válido")
        