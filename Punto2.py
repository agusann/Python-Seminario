cant = int(input("Ingrese cantidad de segundos "))
if cant >= 3600:
    horas = cant // 3600
    minutos = (cant % 3600) // 60
    segundos = cant % 60
    print("HORAS", horas, "minutos", minutos, "segundos", segundos)
elif 59 < cant < 3600:
    horas = 0
    minutos = (cant % 3600) // 60
    segundos = cant % 60
    print("HORAS", horas, "minutos", minutos, "segundos", segundos)
else:
    horas = 0
    minutos = 0
    segundos = cant % 60
    print("HORAS", horas, "minutos", minutos, "segundos", segundos)
