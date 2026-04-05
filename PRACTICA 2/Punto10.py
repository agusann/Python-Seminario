rounds = [
{
'theme': 'Entrada',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
}
},
{
'theme': 'Plato principal',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
}
},
{
'theme': 'Postre',
'scores': {
'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
}
},
{
'theme': 'Cocina internacional',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
}
},
{
'theme': 'Final libre',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
}
}
]

estadisticas = {}
vueltas = 1
for ronda in rounds:
    max_puntaje = -1
    ganador = ""
    scores = ronda["scores"]
    
    for participante, jueces in scores.items():
        #print (participante)
        #print(jueces)
        total = sum(jueces.values())
        #print(total)
        if participante not in estadisticas:
            estadisticas[participante] = {"puntaje_total" : 0,  "rondas_ganadas" : 0, "mejor_ronda" : 0, "prom" : 0 }
            estadisticas[participante]["mejor_ronda"] = total
        if total > estadisticas[participante]['mejor_ronda']:
            estadisticas[participante]['mejor_ronda'] = total
        estadisticas[participante]["puntaje_total"] += total
        if total > max_puntaje:
            max_puntaje = total
            ganador = participante
    estadisticas[ganador]["rondas_ganadas"] +=1
    print("EL GANAADOR DE LA RONDA",vueltas, "es ", ganador, "con Puntaje= ", max_puntaje)
    print("---------------------------------------------------")
    print(estadisticas)
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    
    vueltas +=1
    
for persona in estadisticas:
    datos = estadisticas[persona]
    datos["prom"] = datos["puntaje_total"] / 5
        
print(estadisticas)