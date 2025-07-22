students_list = []
promedy_list = []
for i in range(1, 6):
    student = input("Ingrese el nombre del estudiante\n")
    students_list.append(student)
    notes_list = []
    for x in range(1, 4):
        note = int(input("Introduce su nota\n"))
        notes_list.append(note)
    promedy = (notes_list[0] + notes_list[1] + notes_list[2]) / 3
    print(f"El promedio de  {student} es de {promedy}")
    promedy_list.append(promedy)

index = 0
for i in students_list:
    print(f"{students_list[index]} tiene un promedio de {promedy_list[index]}")
    index += 1

if promedy_list[0] < 70 and promedy_list[1] < 70 and promedy_list[2] < 70 and promedy_list[3] < 70 and promedy_list[4] < 70:
    print("Debido a una curva, todos reciben +5 pts")
    index = 0
    for i in students_list:
        print(f"{students_list[index]} tiene un promedio ahora de {promedy_list[index] + 5}")
        index += 1