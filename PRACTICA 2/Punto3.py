review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""


frase = str(input("Ingrese palabras que considere spolier (separando por coma)"))
frase = frase.split(",")
for i in range(len(frase)):
    frase[i] = frase[i].strip().lower()
#print (frase)
texto = review.split()
nuevo_texto = ""
for palabra in texto:
    for spoiler in frase:
        if (palabra.lower() == spoiler):
            palabra = "*" * len(palabra)
    nuevo_texto += palabra + " "

print(nuevo_texto)