posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"]
tateti=""
hastag=""
dic = {}
for frase in posts:
    tateti = frase.split()
    for palabra in tateti:
        if palabra.startswith("#"):
            hastag = palabra
            if hastag in dic:
                dic[hastag] += 1
            else:
                dic[hastag] = 1
        
print ("hastag con la cantidad de repedtidos")
print(dic)
