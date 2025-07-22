subtotal = 0

while True:
    action = int(input("Ingrese la accion a realizar\n 1. Agregar producto\n 2. Pagar\n"))
    if action == 1:
        price = int(input("Ingrese el precio\n"))
        subtotal += price
    elif action == 2:
        break

tip = int(input("Desea dejar propina?\n 1. Si\n 2. No\n"))
if tip == 1:
    porcent_tip = int(input("Cuanto porcentaje de propina dejará?\n")) / 100
    much_tip = subtotal * porcent_tip
    total_tip = subtotal + much_tip
    print(f"Usted dejará {much_tip} de propina")
elif tip == 2:
    total_tip = subtotal
    print("No se le cargará propina (tacaño)")
    much_tip = 0

tarjet = int(input("Cuenta con tarjeta de cliente frecuente?\n 1. Si\n 2. No\n"))
if tarjet == 1:
    tarjet_disscount = subtotal * 0.1
    print(f"Se le aplicó un descuento de {tarjet_disscount}")
    total_tarjet = total_tip - tarjet_disscount
    print(f"Su total ahora es de {total_tarjet}")
elif tarjet == 2:
    print("Sin tarjeta de cliente")
    total_tarjet = total_tip
    tarjet_disscount = 0

iva = total_tarjet * 0.12
total_iva = total_tarjet + iva

print(f"Sus totales son de:\n"
      f"Subtotal: {subtotal}\n"
      f"Iva: {iva}\n"
      f"Propina: {much_tip}\n"
      f"Descuento con tarjeta {tarjet_disscount}\n"
      f"Total: {total_iva}")

