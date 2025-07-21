name = input("Ingrese su nombre completo\n")
dpi_nums = input("Ingrese su número de dpi\n")
departament = input("Ingrese el departamento donde vive\n").upper()
birth_year = int(input("Ingrese el año en que nació\n"))
can_vote = True

if birth_year < 2008 and departament == "peten" or departament == "alta verapaz":
    can_vote = True

if birth_year > 2007:
    print("Eres menor de edad")
    can_vote = False

if len(name) < 5:
    print("Nombre no valido")
    can_vote = False

if len(dpi_nums) < 13:
    print("DPI no válido")
    can_vote = False

if can_vote:
    print(f"Bienvenido {name}, su centro de votación está en {departament}")
else:
    print("No puedes votar")