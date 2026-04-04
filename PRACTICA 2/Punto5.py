peso = float(input("Ingrese peso del paquete "))
destino = str(input("Ingrese zona del destino (local/regional/nacional) "))
destino = destino.lower()
costo =0
if destino == "local":
    if peso < 1:
        costo=500
    elif 1 < peso < 5:
        costo = 1000
    else: 
        costo = 2000
elif destino == "regional":
    if peso < 1:
        costo=1000
    elif 1 < peso < 5:
        costo = 2500
    else: 
        costo = 5000
elif destino == "nacional":
    if peso < 1:
        costo=2000
    elif 1 < peso < 5:
        costo = 4500
    else: 
        costo = 8000

if costo == 0:
    print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
else:
    print("Costo del envio", costo)
        