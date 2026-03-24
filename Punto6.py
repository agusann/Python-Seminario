num = int(input("Ingrese un numero "))
cinco = []
resto = []
for i in range (1, (num+1)):
    if (i % 5) == 0:
        cinco.append(i)
        #print ("SALTE")
        continue
    else:
     resto.append(i)
    #print ("numero",i)
    
for i in cinco:
    print (i)

print ("////////////////////////////")
for i in resto:
    print (i)
