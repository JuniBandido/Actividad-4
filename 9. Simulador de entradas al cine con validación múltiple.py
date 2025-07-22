age = int(input("Introduzca su edad\n"))
day = input("Introduzca el dia\n").upper
student = int(input("Es estudiante?\n"
                    "1. Si\n"
                    "2. No\n"))

normal_price = 50
student_price = 35

if age < 13:
    print("usted no puede ver esta película")
elif day == "miercoles":
    print("Hoy hay 2x1")
elif student == 1:
    print(f"El total es de Q{student_price}")

