import random
words = {
    "Programacion": ["python","variable", "funcion", "bucle"],
    "Estructuras": ["lista","cadena"],
    "Conceptos": ["programa", "entero"]
}

guessed = []
attempts = 6
print("¡Bienvenido al Ahorcado!")
print ("Vamos a prensentar las categorias")
for categoria in words:
    print(categoria)
    
while True:
    eleccion = input("ingrese categoria ")
    if eleccion in words:
        break
    else:
        print ("Categoria inconrrecta, vuelve a intentarlo")


word = random.sample(words[eleccion])
print()
puntaje=0
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan

    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
     print("¡Ganaste!")
     puntaje += 6
     break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if letter.isalpha() and len(letter)==1:
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            puntaje -= 1
        print()
    else:
        print("Recuerda ingresar solo 1 letra")
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje=0
print("El puntaje es ", {puntaje})