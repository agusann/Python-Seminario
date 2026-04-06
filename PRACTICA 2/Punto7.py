participantes = str(input("INGRESE LISTA DE PARTICIPANTES SEPARADO CON COMA: "))
participantes = participantes.split(",")
repetidos = False
for i in range(len(participantes)):
    participantes[i] = participantes[i].strip().lower()
    for j in range(i+1, len(participantes)):
        if participantes[i] == participantes[j]:
            repetidos = True

import random
if (repetidos == False) and (len(participantes) > 3):
    duplicado = participantes.copy()
    while True:
        ok = True
        random.shuffle(duplicado)
        for i in range(len(participantes)):
            if participantes[i] == duplicado [i]:
                ok=False
        if ok:
            break
    print("----------------------------------")
    print ("SORTEO DEL AMIGO INVISIBLE")
    for i in range(len(participantes)):
     print(participantes[i], "->", duplicado[i])
     print("++++++++++++++++++++++++++++++++++++++")
else:
    print("Debe ingresar al menos 3 participantes que ninguno este repetido")