import time

horas = 0
minutos = 0
segundos = 0

while True:
    time.sleep(1)
    tiempo_actual = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    print(tiempo_actual)
        
    segundos = segundos + 1
    
    # Reinicio
    if segundos == 60:
        segundos = 0
        minutos = minutos + 1
        
        if minutos == 60:
            minutos = 0
            horas = horas + 1
            
            if horas == 24:
                horas = 0