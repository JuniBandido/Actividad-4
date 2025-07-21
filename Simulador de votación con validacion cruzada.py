name = input("Ingrese su nombre completo\n")
dpi_nums = input("Ingrese su número de dpi\n")
departament = input("Ingrese el departamento donde vive\n")
birth_year = int(input("Ingrese el año en que nació\n"))

if birth_year < 2008 and departament == "peten" or departament == "alta verapaz":
    print("peudes votar")
elif birth_year < 2007:
    print("puedes votar")
else:
    print("No podes votar, eres menor de 18 años")

if len(name) < 5:
    print("Nombre no valido")
if len(dpi_nums) < 13:
    print("DPI no válido")