print("Introduce una cantidad monetaria múltiplo de 5 para \nsaber cuál es el mínimo de billetes necesario")
dinero = 0
dinero = int(input())
contador500 = 0
contador200 = 0
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador5 = 0
while dinero%5 != 0 or dinero < 0:
    print("Introduce un número que sea múltiplo de 5 o mayor que 0")
    dinero = int(input())
while dinero-500 >= 0:
    dinero-=500
    contador500+=1
while dinero-200 >= 0:
    dinero-=200
    contador200+=1
while dinero-100 >= 0:
    dinero-=100
    contador100+=1
while dinero-50 >= 0:
    dinero-=50
    contador50+=1
while dinero-20 >= 0:
    dinero-=20
    contador20+=1
while dinero-10 >= 0:
    dinero-=10
    contador10+=1
while dinero-5 >= 0:
    dinero-=5
    contador5+=1
print(f"El importe resulta en \n{contador500} billetes de 500, \n{contador200} billetes de 200, \n{contador100} billetes de 100, \n{contador50} billetes de 50, \n{contador20} billetes de 20, \n{contador10} billetes de 10 y \n{contador5} billetes de 5.")

