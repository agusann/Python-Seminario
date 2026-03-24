palabras = []
while True:
    nombre = input("ingrese palabra ")
    if nombre == "":
        break
    palabras.append(nombre)
    
#for nombre in palabras:
  #  print(nombre)
frase=""

for p in palabras:
    if len(p) >= 3:        
        frase += p + " "
        
print(frase)
print ("hola mundo")
  