def calcular_resultados(rounds):
    totales = {}
    rondas_ganadas = {}
    mejor_ronda = {}

    for ronda in rounds:
        max_puntaje = -1
        ganador_ronda = " "

        for participante, notas in ronda['scores'].items():
            puntajes = notas['judge_1'] + notas['judge_2'] + notas['judge_3']

            if participante not in totales:
                totales[participante] = 0
                rondas_ganadas[participante] = 0
                mejor_ronda[participante] = 0

            totales[participante] += puntajes
            if puntajes > mejor_ronda[participante]:
                mejor_ronda[participante] = puntajes 
                
            if puntajes > max_puntaje:
                max_puntaje = puntajes
                ganador_ronda = participante
        if ganador_ronda:
            rondas_ganadas[ganador_ronda] += 1
            
    totales_ordenados = dict(sorted(totales.items(), key=lambda x: x[1], reverse=True))

    return totales_ordenados, rondas_ganadas, mejor_ronda


def mostrar_tabla_simple(tabla_ordenada):
    print("TABLA FINAL")
    for nombre, puntos in tabla_ordenada.items():
        print(f"{nombre}: {puntos}")


def mostrar_ganador_final(totales_ordenados):
    max_total = 0
    ganador_final = ""

    for participante, total in totales_ordenados.items():
        if total > max_total:
            max_total = total
            ganador_final = participante

    print(f"Ganador final: {ganador_final}")
    print(f"Puntaje del ganador: {max_total}")


def mostrar_tabla_completa(totales, rondas_ganadas, mejor_ronda, rounds):
    cantidad_rondas = len(rounds)
    # Ordenamos para mostrar la tabla de posiciones
    tabla_posiciones = sorted(totales.items(), key=lambda x: x[1], reverse=True)

    print("\nTabla final de posiciones")
    print(f"{'Cocinero':<15} {'Puntaje':<10} {'Rondas G.':<12} {'Mejor R.':<12} {'Promedio':<10}")
    print("-" * 65)

    for participante, total in tabla_posiciones:
        promedio = total / cantidad_rondas
        print(f"{participante:<15} {total:<10} {rondas_ganadas[participante]:<12} {mejor_ronda[participante]:<12} {promedio:<10.2f}")