print("Introduce las horas trabajadas del trabajador para saber el salario y las tasas")
horas = float(input("Introduce las horas "))
salarioHora = float(input("Introduce el salario por hora "))
nombre = input("Introduce el nombre del trabajador ")
tasa = 0
horasExtra = 0
if horas > 35:
    horasExtra = horas - 35
    horas-=horasExtra
salarioBruto = (horas*salarioHora)+(horasExtra*salarioHora)

if salarioBruto <= 500:
    salarioNeto = salarioBruto

if salarioBruto > 500 and salarioBruto < 900:
    tasa = 25
    salarioNeto = salarioBruto-500
    salarioNeto *= tasa/100
    salarioNeto += salarioBruto

if salarioBruto >= 900:
    tasa = 45
    salarioProvisional = 0
    salarioNeto = salarioBruto - 900
    salarioProvisional = salarioNeto
    salarioNeto *= tasa/100
    salarioProvisional = salarioBruto - 500
    salarioProvisional * 25/100
    salarioNeto = salarioNeto + salarioProvisional + salarioBruto

print(f"El trabajador {nombre} tiene un salario bruto de {salarioBruto}, que tras una tasa de impuesto de {tasa} recibirá un salario neto de {salarioNeto}")



