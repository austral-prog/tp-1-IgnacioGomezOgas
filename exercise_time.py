def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """

    total_segundos=3665
    total_minutos=3665/60 #aprox 61,08333...
    horas_completas=total_minutos//60 #es 1 hora, 60 minutos
    print(int(horas_completas)) #uso int para que quede distinto de 1.0
    minutos_restantes=total_minutos-60 #1,08333... minutos
    minutos_completos_restantes=int(minutos_restantes) #1
    print(minutos_completos_restantes)
    segundos_restantes=(minutos_restantes-1)*60 #saca el minuto que usamos, multiplicamos por 60 para obtener los segundos
    print(int(segundos_restantes))


time()
