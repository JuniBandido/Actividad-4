year_income = int(input("Ingrese su cantidad de ingreso anual en GTQ\n"))
dependients = int(input("Ingrese el número de dependientes\n"))

if year_income <= 30000:
    tax = year_income * 0.05
elif 30001 < year_income <= 60000:
    tax = year_income * 0.1
elif 60001 < year_income <= 100000:
    tax = year_income * 0.15
elif year_income > 100000:
    tax = year_income * 0.2

print(f"tu impuesto total es de {tax}")