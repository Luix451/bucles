nombre = str(input("Ingrese su nombre: "))
precio_neto = float(input("Ingrese el precio neto del producto: "))
cantidad_adquirida = int(input("Ingrese la cantidad adquirida: "))
tiene_membresia = input("¿Tiene membresía? (si/no): ").lower() == "si"

if cantidad_adquirida >= 5:
    descuento = 15
    precio_final = precio_neto * cantidad_adquirida - descuento
    print(precio_final)
    
elif cantidad_adquirida >= 5 and tiene_membresia:
    descuento = 25
    precio_final = precio_neto * cantidad_adquirida - descuento
    print(precio_final)
else:
    descuento = 0
    precio_final = precio_neto * cantidad_adquirida
    print(precio_final)