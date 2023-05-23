import time 
import locale
import re
PATTERN = "(\d)+(\D)+(\d)+"
locale.setlocale(locale.LC_TIME, "es_ES") # establecer el locale a español

class Fecha: 

    def __init__(self,anio,mes,dia):
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

    def date_conversion(str):
        # fecha en español con formato d de m de aaaa
        #La fecha de hoy es "3 de mayo de 2022"
        match = re.search(PATTERN, str)
        date_es = match.group()
        date_dt = datetime.strptime(fecha_es, "%d de %B de %Y") # objeto datetime con formato aaaa-mm-dd
        return date_dt


fecha = "8 May, 2023"
fecha= time.strptime(fecha, "%d %B, %Y")
print(contador_fecha(fecha))