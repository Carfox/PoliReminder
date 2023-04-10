import number
import time 


class Date: 
    def __init__(self):
        pass
    

    def contador_fecha(fecha_limite):

        tiempo=time.localtime(time.time())
        mes =  fecha_limite.tm_mon#- tiempo.tm_mon
        dia =  fecha_limite.tm_mday# - tiempo.tm_mday
        anio =  fecha_limite.tm_year# - tiempo.tm_year
        hora =  fecha_limite.tm_hour# - tiempo.tm_hour
        minuto = fecha_limite.tm_min# - tiempo.tm_min
        segundo = fecha_limite.tm_sec# - tiempo.tm_sec
        salida = f"Faltan {dia} dias {hora} hora(s) {minuto} minuto(s) para terminar el 1er Bimestre"
        time.sleep(1)
        return(salida)


fecha = "8 May, 2023"
fecha= time.strptime(fecha, "%d %B, %Y")
print(contador_fecha(fecha))