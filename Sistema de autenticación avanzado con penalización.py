users_list = {"123": "Juan", "456": "roberto", "789": "Maria"}

trys = 0

while True:
    password = input("Ingresa tu contraseña\n")
    while True:
        while password not in users_list:
            trys += 1
            print(f"Contrasñea Incorrecta, has usado {trys} de 3 intentos")
            password = input("Intenta nuevamente\n")
            if trys == 3:
                print("ACCESO BLOQUEADO")
                exit()

        if password in users_list:
            action = input(f"Bienvenido {users_list[password]}, escoge una opcion\n 1. Ver perfil\n 2. Cambiar contraseña\n 3. Cerrar Sesión\n")
            if action == "3":
                print("Cerrando sesion")
                break