price = 35

weight = int(input("Introduzca el peso (kg)\n"))

leng = int(input("introduzca la distancia (km)\n"))

urgence = int(input("Es urgente?\n 1. Si\n 2. No\n"))

size = int(input("Qué tamaño es el paquete?\n 1. pequeño\n 2. mediano\n 3. grande\n"))

if urgence == 1:
    price = price + 50
    print("Debido a la urgencia del paquete, se le cobrará Q35 + Q50")
    print(f"Su nuevo total es de Q{price}")

if size == 3:
    print(f"Debido al tamaño del paquete, se le cobrará Q{price} + Q30")
    price = price + 30
    print(f"Su nuevo total es de Q{price}")

if urgence == 2 and weight < 5:
    print(f"Debido a la sencillez del envio, se le hizo un descuento de Q{price} - Q20")
    price = price - 20

print(f"El total de su envio es de Q{price}")