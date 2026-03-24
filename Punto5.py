total = 0
num = int(input("Ingrese un numero= "))
while num != 0:
    total += num
    num = int(input("Ingrese un numero= "))
    if num == 0:
        break
print("El total es ", total)
    