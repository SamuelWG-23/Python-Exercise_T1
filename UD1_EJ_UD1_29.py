import random
print("Piensa un número entre 1 y 100 para que el programa intente adivinarlo")
print("Menu: \n 1.Mayor \n 2.Menor \n 3.Igual")
num = 0
numeroMenor = 0
numeroMayor = 101
igual = False
numeroAleatorio = 0
respuesta = 0
while igual == False:
    numeroAleatorio = random.randrange(numeroMenor+1,numeroMayor)
    print(f"Es el numero que estas pensando {numeroAleatorio}?")
    respuesta = int(input())
    if respuesta == 2:
        numeroMayor = numeroAleatorio
    elif respuesta == 1:
        numeroMenor = numeroAleatorio
    elif respuesta == 3:
        igual=True
        print("He acertado!")
    else:
        print("Valor no válido")

