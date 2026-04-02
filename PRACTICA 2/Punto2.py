playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]
total_segundos=0
segundos_max=-1
segundos_min=999999
for cancion in playlist:
    duracion = cancion["duration"]
    minutos, segundos = duracion.split(":")
    minutos = int(minutos)
    segundos = int(segundos)
    total_segundos += (minutos * 60) + segundos
    if (((minutos * 60) + segundos) > segundos_max):
        segundos_max = (minutos * 60) + segundos
        cancion_larga = cancion
    elif (((minutos * 60) + segundos) < segundos_min):
        segundos_min = (minutos * 60) + segundos
        cancion_corta = cancion
        

minutos = total_segundos // 60
segundos = total_segundos % 60

print("total de minutos de la playlist", minutos, "m")
print("total de segundos de la playlist", segundos, "s")

print("La cancion mas larga es", cancion_larga)
print("La cancion mas corta es", cancion_corta)