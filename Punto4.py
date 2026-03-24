num = int(input("Ingrese un numero "))
for i in range (1, (num+1)):
    if (i % 5) == 0:
        print ("SALTE")
        continue
    print ("numero",i)