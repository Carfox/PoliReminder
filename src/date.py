import number
import time 

class Date: 
    def __init__(self):
        pass
    

    def check_deadline(deadline):

        tiempo=time.localtime(time.time())
        mes =  deadline.tm_mon#- tiempo.tm_mon
        dia =  deadline.tm_mday# - tiempo.tm_mday
        anio =  deadline.tm_year# - tiempo.tm_year
        hora =  deadline.tm_hour# - tiempo.tm_hour
        minuto = deadline.tm_min# - tiempo.tm_min
        salida = f"Faltan {dia} dias {hora} hora(s) {minuto} minuto(s) para terminar el 1er Bimestre"
        time.sleep(1)
        return(salida)


fecha = "8 May, 2023"
fecha= time.strptime(fecha, "%d %B, %Y")
print(contador_fecha(fecha))