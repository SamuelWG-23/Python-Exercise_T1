print("Introduce las horas trabajadas del trabajador para saber el salario y las tasas")
horas = int(input("Introduce las horas "))
salarioHora = float(input("Introduce el salario por hora "))
nombre = str(input("Introduce el nombre del trabajador "))
salarioOriginal = 0
horasExtra = 0
salarioNeto = 0
tasa = 0
if horas > 35:
    horasExtra = horas - 35
salarioBruto = (horas*salarioHora) + (horasExtra*salarioHora*1.5)
salarioOriginal=salarioBruto

if salarioBruto <= 500:
    salarioNeto = salarioBruto

if salarioBruto > 500 and salarioBruto <= 900:
    salarioNeto = salarioBruto-500
    salarioBruto -= 500
    tasa = salarioBruto*25/100
    salarioNeto = salarioBruto+tasa




print(f"El trabajador {nombre} con un salario bruto de {salarioOriginal} tiene un salario neto de {salarioNeto} y tasas de {tasa} ")